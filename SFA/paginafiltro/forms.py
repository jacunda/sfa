from django import forms

class EmpresasRequest(forms.Form):
   setor = forms.CharField()
   
   LPA = forms.DecimalField()
   LPA_option = forms.CharField()

   crescimento_receita5 = forms.DecimalField()
   crescimento_receita5_option = forms.CharField()

   EBIT12 = forms.DecimalField()
   EBIT12_option = forms.CharField()

   patrim_liq = forms.DecimalField()
   patrim_liq_option = forms.CharField()

   PL = forms.DecimalField()
   PL_option = forms.CharField()

   volume = forms.DecimalField()
   volume_option = forms.CharField()

   Lucro_liq12 = forms.DecimalField()
   Lucro_liq12_option = forms.CharField()

   PVP = forms.DecimalField()
   PVP_option = forms.CharField()

   div_bruta = forms.DecimalField()
   div_bruta_option = forms.CharField()

   receita_liq3 = forms.DecimalField()
   receita_liq3_option = forms.CharField()

   dividend_yield = forms.DecimalField()
   dividend_yield_option = forms.CharField()

   div_liquida = forms.DecimalField()
   div_liquida_option = forms.CharField()

   EBIT3 = forms.DecimalField()
   EBIT3_option = forms.CharField()

   VPA = forms.DecimalField()
   VPA_option = forms.CharField()

   receita_liq12 = forms.DecimalField()
   receita_liq12_option = forms.CharField()

   lucro_liq3 = forms.DecimalField()
   lucro_liq3 = forms.CharField()
 