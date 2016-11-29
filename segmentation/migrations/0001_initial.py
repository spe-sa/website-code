# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthenticatedSegmentPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', max_length=128, verbose_name='label', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CookieSegmentPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', max_length=128, verbose_name='label', blank=True)),
                ('cookie_key', models.CharField(default='', help_text='Name of cookie to consider.', max_length=4096, verbose_name='name of cookie')),
                ('cookie_value', models.CharField(default='', help_text='Value to consider.', max_length=4096, verbose_name='value to compare')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CountrySegmentPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', max_length=128, verbose_name='label', blank=True)),
                ('country_code', models.CharField(default='O1', max_length=2, verbose_name='country', choices=[('A1', 'A1: Anonymous Proxy'), ('A2', 'A2: Satellite Provider'), ('O1', 'O1: Other Country'), ('AD', 'AD: Andorra'), ('AE', 'AE: United Arab Emirates'), ('AF', 'AF: Afghanistan'), ('AG', 'AG: Antigua and Barbuda'), ('AI', 'AI: Anguilla'), ('AL', 'AL: Albania'), ('AM', 'AM: Armenia'), ('AO', 'AO: Angola'), ('AP', 'AP: Asia/Pacific Region'), ('AQ', 'AQ: Antarctica'), ('AR', 'AR: Argentina'), ('AS', 'AS: American Samoa'), ('AT', 'AT: Austria'), ('AU', 'AU: Australia'), ('AW', 'AW: Aruba'), ('AX', 'AX: Aland Islands'), ('AZ', 'AZ: Azerbaijan'), ('BA', 'BA: Bosnia and Herzegovina'), ('BB', 'BB: Barbados'), ('BD', 'BD: Bangladesh'), ('BE', 'BE: Belgium'), ('BF', 'BF: Burkina Faso'), ('BG', 'BG: Bulgaria'), ('BH', 'BH: Bahrain'), ('BI', 'BI: Burundi'), ('BJ', 'BJ: Benin'), ('BL', 'BL: Saint Bartelemey'), ('BM', 'BM: Bermuda'), ('BN', 'BN: Brunei Darussalam'), ('BO', 'BO: Bolivia'), ('BQ', 'BQ: Bonaire, Saint Eustatius and Saba'), ('BR', 'BR: Brazil'), ('BS', 'BS: Bahamas'), ('BT', 'BT: Bhutan'), ('BV', 'BV: Bouvet Island'), ('BW', 'BW: Botswana'), ('BY', 'BY: Belarus'), ('BZ', 'BZ: Belize'), ('CA', 'CA: Canada'), ('CC', 'CC: Cocos (Keeling) Islands'), ('CD', 'CD: Congo, The Democratic Republic of the'), ('CF', 'CF: Central African Republic'), ('CG', 'CG: Congo'), ('CH', 'CH: Switzerland'), ('CI', 'CI: Cote d\u2019Ivoire'), ('CK', 'CK: Cook Islands'), ('CL', 'CL: Chile'), ('CM', 'CM: Cameroon'), ('CN', 'CN: China'), ('CO', 'CO: Colombia'), ('CR', 'CR: Costa Rica'), ('CU', 'CU: Cuba'), ('CV', 'CV: Cape Verde'), ('CW', 'CW: Curacao'), ('CX', 'CX: Christmas Island'), ('CY', 'CY: Cyprus'), ('CZ', 'CZ: Czech Republic'), ('DE', 'DE: Germany'), ('DJ', 'DJ: Djibouti'), ('DK', 'DK: Denmark'), ('DM', 'DM: Dominica'), ('DO', 'DO: Dominican Republic'), ('DZ', 'DZ: Algeria'), ('EC', 'EC: Ecuador'), ('EE', 'EE: Estonia'), ('EG', 'EG: Egypt'), ('EH', 'EH: Western Sahara'), ('ER', 'ER: Eritrea'), ('ES', 'ES: Spain'), ('ET', 'ET: Ethiopia'), ('EU', 'EU: Europe'), ('FI', 'FI: Finland'), ('FJ', 'FJ: Fiji'), ('FK', 'FK: Falkland Islands (Malvinas)'), ('FM', 'FM: Micronesia, Federated States of'), ('FO', 'FO: Faroe Islands'), ('FR', 'FR: France'), ('GA', 'GA: Gabon'), ('GB', 'GB: United Kingdom'), ('GD', 'GD: Grenada'), ('GE', 'GE: Georgia'), ('GF', 'GF: French Guiana'), ('GG', 'GG: Guernsey'), ('GH', 'GH: Ghana'), ('GI', 'GI: Gibraltar'), ('GL', 'GL: Greenland'), ('GM', 'GM: Gambia'), ('GN', 'GN: Guinea'), ('GP', 'GP: Guadeloupe'), ('GQ', 'GQ: Equatorial Guinea'), ('GR', 'GR: Greece'), ('GS', 'GS: South Georgia and the South Sandwich Islands'), ('GT', 'GT: Guatemala'), ('GU', 'GU: Guam'), ('GW', 'GW: Guinea-Bissau'), ('GY', 'GY: Guyana'), ('HK', 'HK: Hong Kong'), ('HM', 'HM: Heard Island and McDonald Islands'), ('HN', 'HN: Honduras'), ('HR', 'HR: Croatia'), ('HT', 'HT: Haiti'), ('HU', 'HU: Hungary'), ('ID', 'ID: Indonesia'), ('IE', 'IE: Ireland'), ('IL', 'IL: Israel'), ('IM', 'IM: Isle of Man'), ('IN', 'IN: India'), ('IO', 'IO: British Indian Ocean Territory'), ('IQ', 'IQ: Iraq'), ('IR', 'IR: Iran, Islamic Republic of'), ('IS', 'IS: Iceland'), ('IT', 'IT: Italy'), ('JE', 'JE: Jersey'), ('JM', 'JM: Jamaica'), ('JO', 'JO: Jordan'), ('JP', 'JP: Japan'), ('KE', 'KE: Kenya'), ('KG', 'KG: Kyrgyzstan'), ('KH', 'KH: Cambodia'), ('KI', 'KI: Kiribati'), ('KM', 'KM: Comoros'), ('KN', 'KN: Saint Kitts and Nevis'), ('KP', 'KP: Korea, Democratic People\u2019s Republic of'), ('KR', 'KR: Korea, Republic of'), ('KW', 'KW: Kuwait'), ('KY', 'KY: Cayman Islands'), ('KZ', 'KZ: Kazakhstan'), ('LA', 'LA: Lao, People\u2019s Democratic Republic of'), ('LB', 'LB: Lebanon'), ('LC', 'LC: Saint Lucia'), ('LI', 'LI: Liechtenstein'), ('LK', 'LK: Sri Lanka'), ('LR', 'LR: Liberia'), ('LS', 'LS: Lesotho'), ('LT', 'LT: Lithuania'), ('LU', 'LU: Luxembourg'), ('LV', 'LV: Latvia'), ('LY', 'LY: Libyan Arab Jamahiriya'), ('MA', 'MA: Morocco'), ('MC', 'MC: Monaco'), ('MD', 'MD: Moldova, Republic of'), ('ME', 'ME: Montenegro'), ('MF', 'MF: Saint Martin'), ('MG', 'MG: Madagascar'), ('MH', 'MH: Marshall Islands'), ('MK', 'MK: Macedonia'), ('ML', 'ML: Mali'), ('MM', 'MM: Myanmar'), ('MN', 'MN: Mongolia'), ('MO', 'MO: Macao'), ('MP', 'MP: Northern Mariana Islands'), ('MQ', 'MQ: Martinique'), ('MR', 'MR: Mauritania'), ('MS', 'MS: Montserrat'), ('MT', 'MT: Malta'), ('MU', 'MU: Mauritius'), ('MV', 'MV: Maldives'), ('MW', 'MW: Malawi'), ('MX', 'MX: Mexico'), ('MY', 'MY: Malaysia'), ('MZ', 'MZ: Mozambique'), ('NA', 'NA: Namibia'), ('NC', 'NC: New Caledonia'), ('NE', 'NE: Niger'), ('NF', 'NF: Norfolk Island'), ('NG', 'NG: Nigeria'), ('NI', 'NI: Nicaragua'), ('NL', 'NL: Netherlands'), ('NO', 'NO: Norway'), ('NP', 'NP: Nepal'), ('NR', 'NR: Nauru'), ('NU', 'NU: Niue'), ('NZ', 'NZ: New Zealand'), ('OM', 'OM: Oman'), ('PA', 'PA: Panama'), ('PE', 'PE: Peru'), ('PF', 'PF: French Polynesia'), ('PG', 'PG: Papua New Guinea'), ('PH', 'PH: Philippines'), ('PK', 'PK: Pakistan'), ('PL', 'PL: Poland'), ('PM', 'PM: Saint Pierre and Miquelon'), ('PN', 'PN: Pitcairn'), ('PR', 'PR: Puerto Rico'), ('PS', 'PS: Palestinian Territory'), ('PT', 'PT: Portugal'), ('PW', 'PW: Palau'), ('PY', 'PY: Paraguay'), ('QA', 'QA: Qatar'), ('RE', 'RE: Reunion'), ('RO', 'RO: Romania'), ('RS', 'RS: Serbia'), ('RU', 'RU: Russian Federation'), ('RW', 'RW: Rwanda'), ('SA', 'SA: Saudi Arabia'), ('SB', 'SB: Solomon Islands'), ('SC', 'SC: Seychelles'), ('SD', 'SD: Sudan'), ('SE', 'SE: Sweden'), ('SG', 'SG: Singapore'), ('SH', 'SH: Saint Helena'), ('SI', 'SI: Slovenia'), ('SJ', 'SJ: Svalbard and Jan Mayen'), ('SK', 'SK: Slovakia'), ('SL', 'SL: Sierra Leone'), ('SM', 'SM: San Marino'), ('SN', 'SN: Senegal'), ('SO', 'SO: Somalia'), ('SR', 'SR: Suriname'), ('SS', 'SS: South Sudan'), ('ST', 'ST: Sao Tome and Principe'), ('SV', 'SV: El Salvador'), ('SX', 'SX: Sint Maarten'), ('SY', 'SY: Syrian Arab Republic'), ('SZ', 'SZ: Swaziland'), ('TC', 'TC: Turks and Caicos Islands'), ('TD', 'TD: Chad'), ('TF', 'TF: French Southern Territories'), ('TG', 'TG: Togo'), ('TH', 'TH: Thailand'), ('TJ', 'TJ: Tajikistan'), ('TK', 'TK: Tokelau'), ('TL', 'TL: Timor-Leste'), ('TM', 'TM: Turkmenistan'), ('TN', 'TN: Tunisia'), ('TO', 'TO: Tonga'), ('TR', 'TR: Turkey'), ('TT', 'TT: Trinidad and Tobago'), ('TV', 'TV: Tuvalu'), ('TW', 'TW: Taiwan'), ('TZ', 'TZ: Tanzania, United Republic of'), ('UA', 'UA: Ukraine'), ('UG', 'UG: Uganda'), ('UM', 'UM: United States Minor Outlying Islands'), ('US', 'US: United States'), ('UY', 'UY: Uruguay'), ('UZ', 'UZ: Uzbekistan'), ('VA', 'VA: Holy See (Vatican City State)'), ('VC', 'VC: Saint Vincent and the Grenadines'), ('VE', 'VE: Venezuela'), ('VG', 'VG: Virgin Islands, British'), ('VI', 'VI: Virgin Islands, U.S.'), ('VN', 'VN: Vietnam'), ('VU', 'VU: Vanuatu'), ('WF', 'WF: Wallis and Futuna'), ('WS', 'WS: Samoa'), ('YE', 'YE: Yemen'), ('YT', 'YT: Mayotte'), ('ZA', 'ZA: South Africa'), ('ZM', 'ZM: Zambia'), ('ZW', 'ZW: Zimbabwe'), ('XX', 'XX: - Country Not Found -'), ('XA', 'XA: - GeoIP not initialized -'), ('XB', 'XB: - Error trying to determine country -')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='DisciplineSegmentPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', max_length=128, verbose_name='label', blank=True)),
                ('discipline', models.CharField(max_length=4, choices=[('D&C', 'Drilling and Completions'), ('HSE', 'Health, Safety, Security, Environment & Social Responsibility'), ('M&I', 'Management & Information'), ('P&O', 'Production & Operations'), ('PFC', 'Projects, Facilities & Construciton'), ('RDD', 'Reservoir Description & Dynamics'), ('UND', 'Undeclared')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FallbackSegmentPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', max_length=128, verbose_name='label', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SegmentLimitPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', help_text='Optionally set a label for this limit block.', max_length=128, verbose_name='label', blank=True)),
                ('max_children', models.PositiveIntegerField(default=1, help_text='Display up to how many matching segments?', verbose_name='# of matches to display')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SwitchSegmentPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', max_length=128, verbose_name='label', blank=True)),
                ('on_off', models.BooleanField(default=True, help_text='Uncheck to always hide child plugins.', verbose_name='Always on?')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='VariableSegmentPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', max_length=128, verbose_name='label', blank=True)),
                ('variable_key', models.CharField(help_text='Name of variable to check.', max_length=500, verbose_name='name of variable')),
                ('variable_value', models.CharField(help_text='Value to consider.', max_length=500, verbose_name='value to compare')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='VisitorClassificationSegmentPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', max_length=128, verbose_name='label', blank=True)),
                ('classification_code', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='VisitorPropertySegmentPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', max_length=128, verbose_name='label', blank=True)),
                ('visitor_key', models.CharField(help_text='Name of customer attribute to check.', max_length=500, verbose_name='name of customer attribute')),
                ('visitor_value', models.CharField(help_text='Date format: 2005-12-31 (year-month-day)', max_length=500, verbose_name='value to compare')),
                ('data_type', models.CharField(default='string', max_length=20, verbose_name='Data type to use for comparison', choices=[('string', 'String'), ('date', 'Date'), ('int', 'Int')])),
                ('operator', models.CharField(default='=', max_length=20, verbose_name='Type of comparison', choices=[('=', '='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<='), ('!=', '!=')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='VisitorSegmentPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', max_length=128, verbose_name='label', blank=True)),
                ('visitor_key', models.CharField(help_text='Name of customer attribute to check.', max_length=500, verbose_name='name of customer attribute')),
                ('visitor_value', models.CharField(help_text='Value to consider.', max_length=500, verbose_name='value to compare')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
