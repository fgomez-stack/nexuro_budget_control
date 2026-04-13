{
    'name': 'Nexuro Budget Control',
    'version': '1.0.0',
    'summary': 'Control de presupuestos por departamento con soporte de adjuntos PDF',
    'description': """
        Modulo avanzado para el control financiero de departamentos. 
        Permite trackear gastos reales contra presupuestos y adjuntar comprobantes físicos.
    """,
    'author': 'Nexuro',
    'website': 'https://www.tuweb.com',
    'category': 'Accounting/Management',
    'license': 'LGPL-3',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/budget_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
