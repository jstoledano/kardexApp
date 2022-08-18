from datetime import timedelta

from django.db import models

TIPO_MATERIA = (
    ('1', 'Obligatoria'),
    ('2', 'Optativa')
)
INICIO: int = 15


class Materia(models.Model):
    clave = models.CharField(max_length=4)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1, choices=TIPO_MATERIA)
    semestre = models.PositiveSmallIntegerField()
    puntos = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materias"

    def __str__(self) -> str:
        return f'{self.clave} {self.nombre}'


class Clase(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='materia_clase')
    periodo = models.CharField(max_length=6)
    grupo = models.CharField(max_length=4)
    asesor = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'

    def __str__(self) -> str:
        return f'{self.materia.clave} - {self.grupo} - {self.materia.nombre} ({self.periodo})'


class Tarea(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='clase_tarea')
    unidad = models.PositiveSmallIntegerField()
    actividad = models.CharField(max_length=2)
    f_inicio = models.DateField(editable=False)
    f_entrega = models.DateField()
    desc = models.TextField()

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self) -> str:
        if self.actividad.isnumeric():
            return f'{self.clase.materia.clave}:{self.unidad:02d}:{int(self.actividad):02d}'
        else:
            return f'{self.clase.materia.clave}:{self.unidad:02d}:{self.actividad}'

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.f_inicio = self.f_entrega - timedelta(days=INICIO)
        super(Tarea, self).save(force_insert, force_update)
