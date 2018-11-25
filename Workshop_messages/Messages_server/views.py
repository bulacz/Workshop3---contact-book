from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from Messages_server.models import Person, Telephone, Adress, Email, Groups


class MainView(View):
    def get(self, request):
        return render(request, "main.html")


def add_person(request):
    if request.method == 'GET':
        return render(request, "add_person.html")
    else:
        name = str(request.POST["name"])
        surname = str(request.POST["surname"])
        description = str(request.POST['description'])
        Person.objects.create(name=name, surname=surname, description=description)
        new_id = Person.objects.latest().id

        return HttpResponseRedirect(f"show/{new_id}")


# obsługa żądania modyfikowania użytkownika.
class ModifyPerson(View):
    def get(self, request, id):
        person_to_midyfy = Person.objects.get(pk=id)
        # request.session['contact_id'] = id  #zapis do sesji informacji o modyfikowanym userze

        # getting person's phones as a list, not a queryset
        persons_telephones = []
        for telephone in person_to_midyfy.telephone_set.all():
            persons_telephones.append(telephone)

        # getting person's emails as list, not a queryset
        persons_emails = []
        for email in person_to_midyfy.email_set.all():
            persons_emails.append(email)

        # sending db values to the form
        ctx = {
            "person": person_to_midyfy,
            "person_id": id,
            "person_name": person_to_midyfy.name,
            "person_surname": person_to_midyfy.surname,
            "person_description": person_to_midyfy.description,
            "persons_phones": persons_telephones,
            "persons_emails": persons_emails,
            "persons_adress": person_to_midyfy.adress,
        }
        return render(request, "modify_person.html", ctx)

    def post(self, request, id):
        person_to_modify = Person.objects.get(pk=id)
        person_to_modify.name = str(request.POST.get("name"))
        person_to_modify.surname = str(request.POST.get("surname"))
        person_to_modify.description = str(request.POST.get("description"))
        person_to_modify.save()

        # handling phone numbers removal
        for doomed_phone in request.POST.getlist('phone_delete'):
            doomed_phone_id = int(doomed_phone)
            phone_to_delete = Telephone.objects.get(pk=doomed_phone_id)
            phone_to_delete.delete()

        # handling email adresses removal
        for doomed_email in request.POST.getlist('email_delete'):
            doomed_email_id = int(doomed_email)
            email_to_delete = Email.objects.get(pk=doomed_email_id)
            email_to_delete.delete()

        # handling adress removal
        if request.POST.get('adress_delete'):
            doomed_adress = Adress.objects.get(pk=request.POST.get('adress_delete'))
            doomed_adress.delete()

        # returning to the site with user_info
        return HttpResponseRedirect(f'/show/{id}')


# obsługa formularza do dodawania adresu zamieszkania
class AddAdress(View):
    def get(self, request, id):
        return render(request, "add_adress.html")

    def post(self, request, id):
        person_to_add_adress = Person.objects.get(pk=id)

        # obsługa braku numeru mieszkania - w logice widoku
        if request.POST["flat"]:
            new_adress = Adress.objects.create(
                city=request.POST.get("city"),
                street=request.POST.get("street"),
                house=request.POST.get("house"),
                flat=request.POST.get("flat"),
            )
        else:
            new_adress = Adress.objects.create(
                city=request.POST.get("city"),
                street=request.POST.get("street"),
                house=request.POST.get("house"),
            )
        person_to_add_adress.adress = new_adress
        person_to_add_adress.save()

        return HttpResponseRedirect(f"/show/{id}")


# obsługa formularza do dodawania adresu e-mail
class AddEmail(View):
    def get(self, request, id):
        return render(request, "add_email.html")

    def post(self, request, id):
        person_to_add_email = Person.objects.get(pk=id)
        new_email = person_to_add_email.email_set.create(
            email_adress=request.POST.get("email_adress"),
            email_description=request.POST.get("email_description")
        )

        return HttpResponseRedirect(f"/show/{id}")


# obsługa formularza do dodawania telefonu
class AddTelephone(View):
    def get(self, request, id):
        return render(request, "add_telephone.html")

    def post(self, request, id):
        person_to_add_telephone = Person.objects.get(pk=id)
        new_phone = person_to_add_telephone.telephone_set.create(
            phone_number=request.POST.get("phone_number"),
            phone_description=request.POST.get("phone_description")
        )

        return HttpResponseRedirect(f"/show/{id}")


# obsługa (po gecie) żadania skasowania użytkownika
def delete_person(request, id):
    if request.method == 'GET':
        try:
            person_to_delete = Person.objects.get(pk=id)
            person_to_delete.delete()

            return HttpResponseRedirect(f'/allusers')

        except Person.DoesNotExist:
            return HttpResponse("No such user")


# obsługa pokazywania użytkownika
def show_person(request, id):
    if request.method == 'GET':
        try:
            person_to_show = Person.objects.get(pk=id)

            # getting person's phones as list, not a queryset
            persons_telephones = []
            for telephone in person_to_show.telephone_set.all():
                persons_telephones.append(telephone)

            # getting person's emails as list, not a queryset
            persons_emails = []
            for email in person_to_show.email_set.all():
                persons_emails.append(email)

            # sending necessary data to .html form
            ctx = {
                "person_id": id,
                "person_name": person_to_show.name,
                "person_surname": person_to_show.surname,
                "person_description": person_to_show.description,
                "persons_phones": persons_telephones,
                "persons_emails": persons_emails,
                "persons_adress": person_to_show.adress,
            }

            return render(request, "show_person.html", ctx)

        except Person.DoesNotExist:
            return HttpResponse("No such user")


# obsługa żądania wyświetlenia wszystkich użytkowników
def show_all(request):
    if request.method == 'GET':
        all_people = Person.objects.order_by("surname")
        ctx = {
            "all_people": all_people,
        }

        return render(request, "show_all_users.html", ctx)


def show_all_groups(request):
    if request.method == 'GET':
        groups = Groups.objects.all().order_by("group_name")
        people = Person.objects.all().order_by("surname")
        group_list = []
        for each_group in groups:
            group_list.append(each_group)

        ctx = {
            "groups": groups,
            "people": people,
            "group_list": group_list,
        }

        return render(request, "show_all_groups.html", ctx)

    else:
        Groups.objects.create(group_name=request.POST.get('group_name'))

        return HttpResponseRedirect("/allGroups")


class AddContactToGroup(View):
    def get(self, request):
        all_contacts = Person.objects.all().order_by("surname")
        all_groups = Groups.objects.all().order_by("group_name")

        ctx = {
            "all_contacts": all_contacts,
            "all_groups": all_groups,
        }

        return render(request, "add_contact_to_group.html", ctx)

    def post(self, request):
        selected_user = Person.objects.get(pk=request.POST.get('person'))
        selected_groups = request.POST.getlist('groups')
        group_counter = 0
        while group_counter < len(selected_groups):
            selected_user.group.add(Groups.objects.get(pk=selected_groups[group_counter]))
            group_counter += 1

        return HttpResponseRedirect('/personInGroups')


class GroupSearch(View):
    def post(self, request):
        try:
            person_name = request.POST.get('contact_name')  # pobranie imienia osoby z POSTa
            person_surname = request.POST.get('contact_surname')  # pobranie nazwiska osoby z POSTa
            people = Person.objects.filter(name__contains=person_name). \
                filter(surname__contains=person_surname).order_by("surname")
            if people:
                ctx = {
                    "people": people,
                }
            else:
                raise Http404
            return render(request, "person_in_groups.html", ctx)
        except AttributeError:
            return Http404

    def get(self, request):
        return render(request, "group-search.html")


class PersonInGroups(View):
    def get(self, request):
        contacts = Person.objects.all().order_by("surname")
        ctx = {"people": contacts}
        return render(request, "show_all_contacts_groups.html", ctx)
