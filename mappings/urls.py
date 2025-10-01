from django.urls import path
from .views import MappingListCreateView, MappingDetailView, PatientDoctorListView

urlpatterns = [
    path('', MappingListCreateView.as_view(), name='mapping-list-create'),   # POST /api/mappings/ + GET all mappings
    path('<int:pk>/', MappingDetailView.as_view(), name='mapping-detail'),   # DELETE /api/mappings/<id>/
    path('<int:patient_id>/doctors/', PatientDoctorListView.as_view(), name='patient-doctors'),  # GET doctors of a patient
]
