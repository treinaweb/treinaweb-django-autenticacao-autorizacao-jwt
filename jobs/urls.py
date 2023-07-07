from django.urls import path

from .views import JobList, JobDetail, JobApplicantsView


app_name = "jobs"
urlpatterns = [
    path("", JobList.as_view(), name="list"),
    path("<int:pk>", JobDetail.as_view(), name="detail"),
    path("<int:pk>/applicants/", JobApplicantsView.as_view(), name="applicants"),
]
