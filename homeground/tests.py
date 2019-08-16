# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Resident,Business,tags

# Create your tests here.
class ResidentTestClass(TestCase):
    def setUp(self):
        self.charles= Resident(first_name = 'charles', last_name = 'maina')

    def test_instance(self):
        self.assertTrue(isinstance(self.charles,Resident))

    def test_save_method(self):
        self.charles.save_resident()
        resident = Resident.objects.all()
        self.assertTrue(len(resident) > 0)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.charles= Resident(first_name = 'charles', last_name = 'maina')
        self.save.charles.save_resident()

        self.new_tag = tags(name ='testing')
        self.new_tag.save()

        self.new_business= Business(title ='Test Buiness',post = 'This is a random test Post', resident = self.charles)
        self.new_business.save()

        self.new_business.tags.add(self.new_tag)

    def tearDown(self):
        Resident.objects.all().delete()
        tags.objects.all().delete()
        Business.objects.all().delete()