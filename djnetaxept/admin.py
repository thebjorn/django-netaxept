from django.contrib import admin
from djnetaxept.models import NetaxeptPayment, NetaxeptTransaction


class NetaxeptPaymentOptions(admin.ModelAdmin):
    list_display = """id transaction_id amount currencycode description
                      ordernumber flagged responsecode responsesource
                      responsetext""".split()


class NetaxeptTransactionOptions(admin.ModelAdmin):
    list_display = """id transaction_id operation amount flagged responsecode
                      responsesource responsetext""".split()


admin.site.register(NetaxeptPayment, NetaxeptPaymentOptions)
admin.site.register(NetaxeptTransaction, NetaxeptTransactionOptions)
