
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import DxSerializer, MedSerializer, LabSerializer, PxSerializer, FxSerializer, EventSerializer
from django.shortcuts import render

from .models import Dx, Lab, Med, Px, Fx, Event

class DxAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Dx.objects.all()
    serializer_class = DxSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class DxCaseAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Dx.objects.all()
    serializer_class = DxSerializer

    def get(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.list(request)

    def post(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.create(request)

    def delete(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.destroy(request)

    def set_query_by_number(self, number: int):
        case = 'Case ' + str(number)
        self.queryset = Dx.objects.filter(number=case)

class DxDetailAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Dx.objects.all()
    serializer_class = DxSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, partial=True)

    def patch(self, request: Request, pk: int):
        return self.update(request, partial=True)

    def delete(self, request: Request, pk: int):
        return self.destroy(request)

class LabAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class LabCaseAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer

    def get(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.list(request)

    def post(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.create(request)

    def delete(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.destroy(request)

    def set_query_by_number(self, number: int):
        case = 'Case ' + str(number)
        self.queryset = Lab.objects.filter(number=case)

class LabDetailAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, partial=True)

    def patch(self, request: Request, pk: int):
        return self.update(request, partial=True)

    def delete(self, request: Request, pk: int):
        return self.destroy(request)

class MedAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Med.objects.all()
    serializer_class = MedSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class MedCaseAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Med.objects.all()
    serializer_class = MedSerializer

    def get(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.list(request)

    def post(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.create(request)

    def delete(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.destroy(request)

    def set_query_by_number(self, number: int):
        case = 'Case ' + str(number)
        self.queryset = Med.objects.filter(number=case)

class MedDetailAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Med.objects.all()
    serializer_class = MedSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, partial=True)

    def patch(self, request: Request, pk: int):
        return self.update(request, partial=True)

    def delete(self, request: Request, pk: int):
        return self.destroy(request)

class PxAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Px.objects.all()
    serializedr_class = PxSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class PxCaseAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Px.objects.all()
    serializer_class = DxSerializer

    def get(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.list(request)

    def post(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.create(request)

    def delete(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.destroy(request)

    def set_query_by_number(self, number: int):
        case = 'Case ' + str(number)
        self.queryset = Px.objects.filter(number=case)

class PxDetailAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Px.objects.all()
    serializer_class = PxSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, partial=True)

    def patch(self, request: Request, pk: int):
        return self.update(request, partial=True)

    def delete(self, request: Request, pk: int):
        return self.destroy(request)

class FxAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Fx.objects.all()
    serializer_class = FxSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class FxCaseAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Fx.objects.all()
    serializer_class = DxSerializer

    def get(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.list(request)

    def post(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.create(request)

    def delete(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.destroy(request)

    def set_query_by_number(self, number: int):
        case = 'Case ' + str(number)
        self.queryset = Fx.objects.filter(number=case)

class FxDetailAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Fx.objects.all()
    serializer_class = FxSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, partial=True)

    def patch(self, request: Request, pk: int):
        return self.update(request, partial=True)

    def delete(self, request: Request, pk: int):
        return self.destroy(request)


class EventAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class EventCaseAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.list(request)

    def post(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.create(request)

    def delete(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.destroy(request)

    def set_query_by_number(self, number: int):
        case = 'Case ' + str(number)
        self.queryset = Event.objects.filter(number=case)


def index(request):
    return render(request, 'manager/index.html')


def create_concate_db(request):
    pass



def concate_db(request, number):
    if(request.method == "CREATE"):
        pass
