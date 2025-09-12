# pagina/migrations/0008_seed_planos.py

from django.db import migrations

def create_default_plans(apps, schema_editor):
    Planos = apps.get_model('pagina', 'Planos')
    
    planos = [
        {
            'titulo': 'Plano Gratuito',
            'descricao': 'Aproveite nossas vantagens',
            'beneficios': 'Lorem ipsum dolor sit amet...',
            'preco': 0.00,
            'tipo': 'gratis',
            'icone_url': 'Images/img-gratis-plan.png',
        },
        {
            'titulo': 'Plano Duo',
            'descricao': 'Para você & Alguém especial',
            'beneficios': 'Lorem ipsum dolor sit amet...',
            'preco': 49.90,
            'tipo': 'duo',
            'icone_url': 'Images/img-duo-plan.png',
        },
        {
            'titulo': 'Plano Angelical',
            'descricao': 'Premium',
            'beneficios': 'Lorem ipsum dolor sit amet...',
            'preco': 99.90,
            'tipo': 'angelical',
            'icone_url': 'Images/img-premium-plan.png',
        },
    ]

    for plano in planos:
        Planos.objects.create(**plano)

class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0007_beneficio_hero_alter_usuario_options_and_more'),  # substitua '…' pelo nome completo da sua migração 007
    ]

    operations = [
        migrations.RunPython(create_default_plans),
    ]
