# -*- coding: utf-8 -*-
{
    'name': 'Приходная накладная для Украины - purchase Order Report Ukrainian ',
    'author': 'Hlv Team Ukraine',
    'website': 'https://hlv-ua.pro',
    'category': 'purchases',
    'depends': ['purchase'],
    'version': '1.0',
    'license': 'Other proprietary',
    'price': 0,
    'currency': 'UAH',
    'description': """
Друкована форма пропозиції продажу та видаткової накладної 
=======================================
Модуль встановлює форму для другу комерційної пропозиції
та договору на поставки. 
Аналог документа в 1С Заказ поставщику и Поступление товаров и услуг
""",
    'auto_install': False,
    'demo': [],
    'data': [
            'views/report_purchaseorder.xml',
            'views/report_purchasequotation.xml',
            'data/purchase_report.xml'
        ],
    'installable': True,
    'application': True,
}
