from django.db import models

# Create your models here.
class Cliente(models.Model):
    sexo_choices = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções"),
    )

    nome =models.CharField(max_length=100,null= False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao= models.CharField(max_length=50, null= False, blank= False)
    sexo = models.CharField(max_length=1,choices=sexo_choices ,null= False,blank= False)

    def __str__(self):
        return  self.nome


