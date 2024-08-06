{
    'name': 'tes satu',
    'version': '1.0',
    'description': '',
    'summary': '',
    'author': '',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'base','web'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/satu.xml',
        # 'static/src/todo_list.js',
        # 'static/src/todo_list.xml',
    ],
    'auto_install': False,
    'application': False,
    'assets': {
        'web.assets_backend': [
            'tes_satu/static/src/*.js',
            'tes_satu/static/src/*xml'
        ]
    }
}