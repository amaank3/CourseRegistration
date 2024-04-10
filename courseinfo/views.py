from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from courseinfo.models import (Instructor, Section, Registration, Student, Semester, Course)
from courseinfo.forms import InstructorForm, SectionForm, CourseForm, StudentForm, RegistrationForm, SemesterForm
from courseinfo.utils import PageLinksMixin


# Create your views here.

class InstructorList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Instructor

class InstructorDetail(DetailView):
    model = Instructor
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        instructor = self.get_object()
        section_list = instructor.sections.all()
        context["section_list"] = section_list
        return context


class InstructorCreate(CreateView):
    form_class = InstructorForm
    model = Instructor


class InstructorUpdate(UpdateView):
    form_class = InstructorForm
    model = Instructor
    template_name = 'courseinfo/instructor_form_update.html'

class InstructorDelete(DeleteView):
    model = Instructor
    success_url = reverse_lazy('courseinfo_registration_list_urlpattern')
    def get(self, request, pk):
        instructor = get_object_or_404(Instructor,pk=pk)
        sections = instructor.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/instructor_refuse_delete.html',
                {'instructor': instructor,
                 'sections': sections,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/instructor_confirm_delete.html',
                {'instructor': instructor}
            )





class SectionList(ListView):
    model = Section


class SectionDetail(DetailView):
    model = Section
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        section = self.get_object()
        context['section'] = section
        context['semester'] = section.semester
        context['course'] = section.course
        context['instructor'] = section.instructor
        context['registration_list'] = section.registrations.all()
        return context



class SectionCreate(CreateView):
    form_class = SectionForm
    model = Section

class SectionUpdate(UpdateView):
    form_class = SectionForm
    model = Section
    template_name = 'courseinfo/section_form_update.html'

class SectionDelete(DeleteView):
    model = Section
    success_url = reverse_lazy('courseinfo_section_list_urlpattern')
    def get(self, request, pk):
        section = get_object_or_404(Section, pk=pk)
        registrations = section.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/section_refuse_delete.html',
                {'section': section, 'registrations': registrations}
            )
        else:
            return render(
                request,
                'courseinfo/section_confirm_delete.html',
                {'section': section}
            )



class RegistrationList(ListView):
    model = Registration

class RegistrationDetail(DetailView):
    model = Registration
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        registration = self.get_object()
        context['student'] = registration.student
        context['section'] = registration.section
        return context


class RegistrationCreate(CreateView):
    form_class = RegistrationForm
    model = Registration

class RegistrationUpdate(UpdateView):
    form_class = RegistrationForm
    model = Registration
    template_name = 'courseinfo/registration_form_update.html'


class RegistrationDelete(DeleteView):
    model = Registration
    success_url = reverse_lazy('courseinfo_registration_list_urlpattern')

class StudentList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Student

class StudentDetail(DetailView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.get_object()
        registration_list = student.registrations.all()
        context["registration_list"] = registration_list
        return context


class StudentCreate(CreateView):
    form_class = StudentForm
    model = Student


class StudentUpdate(UpdateView):
    form_class = StudentForm
    model = Student
    template_name = 'courseinfo/student_form_update.html'

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('courseinfo_student_list_urlpattern')
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        registrations = student.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/student_refuse_delete.html',
                {'student': student, 'registrations': registrations}
            )
        else:
            return render(
                request,
                'courseinfo/student_confirm_delete.html',
                {'student': student}
            )



class SemesterList(ListView):
    model = Semester


class SemesterDetail(DetailView):
    model = Semester
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        semester = self.get_object()
        section_list = semester.sections.all()
        context["section_list"] = section_list
        return context


class SemesterCreate(CreateView):
    form_class = SemesterForm
    model = Semester

class SemesterUpdate(UpdateView):
    form_class = SemesterForm
    model = Semester
    template_name = 'courseinfo/semester_form_update.html'

class SemesterDelete(DeleteView):
    model = Semester
    success_url = reverse_lazy('courseinfo_semester_list_urlpattern')
    def get(self, request, pk):
        semester = get_object_or_404(Semester, pk=pk)
        sections = semester.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/semester_refuse_delete.html',
                {'semester': semester, 'sections': sections}
            )
        else:
            return render(
                request,
                'courseinfo/semester_confirm_delete.html',
                {'semester': semester}
            )


class CourseList(ListView):
    model = Course

class CourseDetail(DetailView):
    model = Course
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        section_list = course.sections.all()
        context["section_list"] = section_list
        return context


class CourseCreate(CreateView):
    form_class = CourseForm
    model = Course


class CourseUpdate(UpdateView):
    form_class = CourseForm
    model = Course
    template_name = 'courseinfo/course_form_update.html'

class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courseinfo_course_list_urlpattern')
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        sections = course.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/course_refuse_delete.html',
                {'course': course, 'sections': sections}
            )
        else:
            return render(
                request,
                'courseinfo/course_confirm_delete.html',
                {'course': course}
            )

