
from django.contrib import admin
from django.urls import path
from courseinfo.views import (
    InstructorList, SectionList, RegistrationList, StudentList, SemesterList, CourseList, InstructorDetail,
    SectionDetail, SemesterDetail, CourseDetail, StudentDetail, RegistrationDetail
)

urlpatterns = [

    path('instructor/',
         InstructorList.as_view(),
         name='courseinfo_instructor_list_urlpattern'),

    path('instructor/<int:pk>/',
         InstructorDetail.as_view(),
         name='courseinfo_instructor_list_urlpattern'),

    path('section/',
         SectionList.as_view(),
         name='courseinfo_section_list_urlpattern'),

    path('section/<int:pk>/',
         SectionDetail.as_view(),
         name='courseinfo_section_list_urlpattern'),

    path('registration/',
         RegistrationList.as_view(),
         name='courseinfo_registration_list_urlpattern'),

    path('registration/<int:pk>/',
         RegistrationDetail.as_view(),
         name='courseinfo_registration_list_urlpattern'),

    path('student/',
         StudentList.as_view(),
         name='courseinfo_student_list_urlpattern'),

    path('student/<int:pk>/',
         StudentDetail.as_view(),
         name='courseinfo_student_list_urlpattern'),

    path('semester/',
         SemesterList.as_view(),
         name='courseinfo_semester_list_urlpattern'),

    path('semester/<int:pk>/',
         SemesterDetail.as_view(),
         name='courseinfo_semester_list_urlpattern'),

    path('course/',
         CourseList.as_view(),
         name='courseinfo_course_list_urlpattern'),

    path('course/<int:pk>/',
         CourseDetail.as_view(),
         name='courseinfo_course_list_urlpattern'),
    ]