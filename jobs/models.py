from django.db import models

# Create your models here.

class Jugador(models.Model):
    DISTRIT = (
    ('Comas','Comas'),
    ('Los Olivos','Los Olivos'),
    ('San Martín de Porres','San Martín de Porres'),
    )
    POSITION =(
    ('Arco','Arco'),
    ('Defensa','Defensa'),
    ('Mediocampo','Mediocampo'),
    ('Ataque','Ataque'),
    ('Mixto','Mixto'),
    )
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    nick=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=20)
    distrito=models.CharField(max_length=100,choices= DISTRIT) 
    posicion=models.CharField(max_length=20,choices= POSITION)
    descripcion=models.TextField()
    password=models.CharField(max_length=156)

    def  __str__(self):
        return self.nick

class Cancha(models.Model):
    DISTRIT = (
    ('Comas','Comas'),
    ('Los Olivos','Los Olivos'),
    ('San Martín de Porres','San Martín de Porres'),
    )
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=200)
    distrito=models.CharField(max_length=100,choices= DISTRIT)
    telefono=models.CharField(max_length=20,name='teléfono')
    ubicacion=models.CharField(max_length=500,name='Ubicación',null=True)
    costoHora=models.DecimalField(decimal_places=2,max_digits=6,name='costo_por_hora')
    jugadoresMaximos=models.IntegerField(name='jugadores_por_equipo')
    
    def  __str__(self):
        return self.nombre

class Juego(models.Model):
    STATUS = (
    ('Activo','Activo'),
    ('Realizado','Realizado'),
    ('Cancelado','Cancelado'),
    )
    estado=models.CharField(max_length=100,choices= STATUS)
    fecha=models.DateField()
    hora=models.TimeField()
    cancha=models.ForeignKey(Cancha,on_delete=models.CASCADE)
    jugador=models.ManyToManyField(Jugador)
    descripcion=models.TextField(null=True)

    def  __str__(self):
        return self.cancha.nombre
