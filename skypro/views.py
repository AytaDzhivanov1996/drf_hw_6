import requests
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings
from skypro.models import Course, Lesson, Subscription, Payment, PaymentLog
from skypro.permissions import OwnerOrStaff
from skypro.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from users.models import User


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [OwnerOrStaff, IsAuthenticated]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [OwnerOrStaff, IsAuthenticated]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(status=Subscription.STATUS_ACTIVE)


class SubscriptionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(status=Subscription.STATUS_INACTIVE)


class PaymentAPIView(APIView):

    def get(self, *args, **kwargs):
        course_pk = self.kwargs.get('pk')
        course_item = get_object_or_404(Course, pk=course_pk)

        payment = Payment.objects.create(
            user=self.request.user,
            paid_course=course_item,
            payment_amount=course_item.price,
            payment_method=Payment.CARD
        )

        user = User.objects.filter(email=self.request.user).first()

        data_for_request = {
            "TerminalKey": settings.TERMINAL_KEY,
            "Amount": course_item.price,
            "OrderId": payment.pk,
            "Description": "Лучший курс на рынке",
            "DATA": {
                "Phone": "+71234567890",
                "Email": user.email
            },
            "Receipt": {
                "Email": user.email,
                "Phone": user.telephone,
                "EmailCompany": "b@test.ru",
                "Taxation": "osn",
                "Items": [
                    {
                        "Name": course_item.title,
                        "Price": course_item.price,
                        "Quantity": 1.00,
                        "Amount": course_item.price,
                        "PaymentMethod": "full_prepayment",
                        "PaymentObject": "commodity",
                        "Tax": "vat10",
                        "Ean13": "0123456789"
                    }
                ]
            }
        }

        response = requests.post(
            'https://securepay.tinkoff.ru/v2/Init',
            json=data_for_request
        )

        return Response(response.json().get('PaymentURL'))
