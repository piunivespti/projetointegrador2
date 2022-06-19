from django.db import models

# Create your models here.
class produto(models.Model):
    id = models.AutoField(primary_key=True)
    ncm = models.IntegerField(verbose_name='NCM')
    desc = models.CharField(max_length=100,verbose_name='Descrição')
    ii = models.FloatField(verbose_name='Imposto de Importação')
    ipi = models.FloatField(verbose_name='Imposto sobre Produto Industrializado')
    pis = models.FloatField(verbose_name='PIS')
    cofins = models.FloatField(verbose_name='COFINS')
    icms = models.FloatField(verbose_name='ICMS')
    imagem = models.ImageField(verbose_name='Imagem', upload_to = 'imagens/', null=True)
    
    def __str__(self):
        fila = "Produto: " + self.desc 
        return fila

    def delete(self, using=None, keep_parents = False):
        self.imagem.storage.delete(self.imagem.name)
        super().delete()
