from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import AdminDateWidget 
import datetime
from .models import *
from django.contrib.auth.models import User

class NewBoxForm(object):
    """docstring for NewBoxForm"""
    serialnumber = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Serial number"))
    password = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Password"))
    

# CHOICES = (("Bankrupt", "Bankrupt"),("b", "B"),)

# class NewAccountForm(forms.Form):

#     since = forms.DateField(initial=datetime.date.today,widget=forms.TextInput({}),label=_("Since"))
#     until = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker2',}),label=_("Until"))
#     block_code = forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={}))

# class SearchAccountForm(forms.Form):
#     since = forms.DateField(initial=datetime.date.today,widget=forms.TextInput({}),label=_("Since"))
#     until = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker2',}),label=_("Until"))
#     block_code = forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={}))

# class CaseListForm(forms.Form):
#     since = forms.DateField(initial=datetime.date.today,widget=forms.TextInput({}),label=_("Since"))
#     until = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker2',}),label=_("Until"))
#     preparation = forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={}))

# class CreateCaseForm(forms.Form):
#     existing_case = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_(""))
#     # team = forms.ModelChoiceField(queryset=Team.objects.all(), empty_label="(Nothing)")
#     attormy = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Attorney"))
   

# class SearchCaseForm(forms.Form):
#     since = forms.DateField(initial=datetime.date.today,widget=forms.TextInput({}),label=_("Since"))
#     until = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker2',}),label=_("Until"))
#     preparation = forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={}))

# class CreateActivityForm(forms.Form):
#     code = forms.CharField(max_length=20,widget=forms.Textarea({}))
#     description = forms.CharField(max_length=100,label=_("Detail"))
#     outcome = forms.CharField(max_length=100,widget=forms.Textarea({}),label=_("Detail"))
#     category = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Activity category"))
#     paticipant = forms.CharField(max_length=50,widget=forms.Textarea({}),label=_("Paticipant"))
#     expense = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Expense"))
#     remark = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Remark"))
#     court_case = forms.ModelChoiceField(queryset=Case.objects.all(), empty_label="(Nothing)")
#     owner = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="(Nothing)")

# class NewTrialCourtForm(forms.Form):
#     attorney_office = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Attorney office"))
#     attorney_office_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker',}),label=_("Attorney date"))
#     letter_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker2',}),label=_("Letter date"))
#     sue_assign_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker3',}),label=_("Sue assign date"))
#     sue_approve_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker4',}),label=_("Sue approve date"))
#     sue_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker5',}),label=_("Sue date"))
#     undecided_case_number = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Undecided case#"))
#     decided_case_number = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Decided case#"))
#     court_area = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Court area"))
#     reconcile_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker6',}),label=_("Eeconcile date"))
#     sentence_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker7',}),label=_("Sentence date"))
#     subrogation_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker8',}),label=_("Subrogation date"))
#     prescription_expire_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker9',}),label=_("Prescription expire date"))
#     sentence_retrive_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker10',}),label=_("Sentence retreive date"))
#     withdraw_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker11',}),label=_("Withdraw date"))
#     principle_capital = forms.FloatField(max_value=15,widget=forms.TextInput({}),label=_("Principle capital"))
#     interest_capital = forms.FloatField(max_value=15, widget=forms.TextInput({}),label=_("Interest capital"))
#     forfeit_capital = forms.FloatField(max_value=15, widget=forms.TextInput({}),label=_("Forfeit capital"))
#     total_capital = forms.FloatField(max_value=15, widget=forms.TextInput({}),label=_("Total capital"))
#     interest_rate = forms.FloatField(max_value=15, widget=forms.TextInput({}),label=_("Interest rate"))
#     sentence_memo = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Sentence memo"))
#     created_by = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="(Nothing)")
#     created_at = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker12',}),label=_("Created at "))
#     updated_at = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker13',}),label=_("Update at"))
        
# class NewAppealCourtForm(forms.Form):
#     appeal_order_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker',}),label=_("Appeal order date"))
#     attorney_appeal_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker2',}),label=_("Attorney appeal date"))
#     case_number = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Case#"))
#     appeal_sentence_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker3',}),label=_("Appeal sentence date"))
#     stay_of_appeal_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker4',}),label=_("Stay of appeal date"))
#     dika_order_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker5',}),label=_("Dika oder date"))
#     attorney_dika_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker6',}),label=_("Attorney dika date"))
#     stay_of_dika_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker7',}),label=_("Attorney dika date"))
#     dika_sentence_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker8',}),label=_("Dika sentence date"))
#     sentence_memo = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Sentence memo"))
#     created_by = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="(Nothing)")
#     created_at = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker9',}),label=_("Created at "))
#     updated_at = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker10',}),label=_("Update at"))
        
# class NewExecutionForm(forms.Form):
#     write_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker',}),label=_("Write datee"))
#     executing_officer_assign_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker2',}),label=_("Executing officer assign date"))
#     executing_officer_name = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Executing officer name"))
#     share_res_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker3',}),label=_("Share res date"))
#     debt_compound_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker4',}),label=_("Debt compound date"))
#     investigating_officer_name = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Investigating officer name"))
#     undischarged_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker5',}),label=_("Undischarged date"))
#     memo = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Memo"))
#     created_by = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="(Nothing)")
#     created_at = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker9',}),label=_("Created at "))
#     updated_at = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker10',}),label=_("Update at"))
        
# class NewBankruptcyForm(forms.Form):
#     letter_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker',}),label=_("Letter date"))
#     sue_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker2',}),label=_("Sue date"))
#     receivership_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker3',}),label=_("Receivership date"))
#     collection_tender_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker4',}),label=_("Collection tender date"))
#     sentence_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker5',}),label=_("Sentence date"))
#     bankruptcy_officer_name = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Bankruptcy officer name "))
#     undecided_case_number = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Undecided case#"))
#     attorney_name = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Attorney name"))
#     decided_case_number = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Decided case#"))
#     prosecution_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker6',}),label=_("Prosecution date"))
#     principle_capital = forms.FloatField(max_value=15,widget=forms.TextInput({}),label=_("Principle capital"))
#     interest_capital = forms.FloatField(max_value=15, widget=forms.TextInput({}),label=_("Interest capital"))
#     forfeit_capital = forms.FloatField(max_value=15, widget=forms.TextInput({}),label=_("Forfeit capital"))
#     total_capital = forms.FloatField(max_value=15, widget=forms.TextInput({}),label=_("Total capital"))
#     memo = forms.CharField(max_length=50,widget=forms.TextInput({}),label=_("Memo"))
#     auction_date = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker7',}),label=_("Auction date"))
#     auction_due = forms.FloatField(max_value=15, widget=forms.TextInput({}),label=_("Auction due"))
#     created_by = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="(Nothing)")
#     created_at = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker12',}),label=_("Created at "))
#     updated_at = forms.DateField(initial=datetime.date.today,widget=forms.TextInput(attrs={'id':'datepicker13',}),label=_("Update at"))

# class PersonForm(forms.Form):

# 	cid = forms.CharField(max_length=13,widget=forms.TextInput(attrs={}),label=_("CID"))
# 	date_of_birth = forms.DateField()
	
# class PersonAttributeForm(forms.Form):

# 	cid = forms.CharField(max_length=13,widget=forms.TextInput(attrs={}),label=_("CID"))
# 	date_of_birth = forms.DateField()


# class CreateCasesForm(forms.Form):
	
# 	case = forms.ModelChoiceField(queryset=Case.objects.all().values_list('id', flat=True).order_by('id'), initial={'value': 'case'},widget=forms.Select(attrs={'class':'form-control caseclass','id':'case','name' : 'case'}))
	# team = forms.ModelChoiceField(queryset=Group.objects.all(),initial={'value': 'team'},widget=forms.Select(attrs={'class':'form-control','style':'height:30px','id':'team'}))