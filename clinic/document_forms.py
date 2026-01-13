PRIMARY_VISIT_FIELDS = [
    {'code': 'complaints', 'label': 'Жалобы', 'type': 'textarea'},
    {'code': 'anamnesis_morbi', 'label': 'Анамнез заболевания', 'type': 'textarea'},
    {'code': 'anamnesis_vitae', 'label': 'Анамнез жизни', 'type': 'textarea'},
    {'code': 'local_status', 'label': 'Локальный статус', 'type': 'textarea'},
    {'code': 'palpation', 'label': 'Пальпация', 'type': 'textarea'},
    {'code': 'height', 'label': 'Рост (см)', 'type': 'number'},
    {'code': 'weight', 'label': 'Вес (кг)', 'type': 'number'},
    {'code': 'pulse', 'label': 'ЧСС', 'type': 'number'},
    {'code': 'od_os', 'label': 'OD / OS', 'type': 'text'},
    {'code': 'additional_info', 'label': 'Дополнительные сведения', 'type': 'textarea'},
    {'code': 'conclusion', 'label': 'Заключение', 'type': 'textarea'},
]

HEAD_DOCTOR_REVIEW_FIELDS = PRIMARY_VISIT_FIELDS + [
    {
        'code': 'operation_decision',
        'label': 'Решение заведующего',
        'type': 'select',
        'options': ['Операция', 'Без операции']
    }
]

PREOPERATIVE_EPICRISIS_FIELDS = PRIMARY_VISIT_FIELDS + [
    {'code': 'planned_operation', 'label': 'Планируемая операция', 'type': 'textarea'},
    {'code': 'planned_anesthesia', 'label': 'Планируемая анестезия', 'type': 'text'},
    {
        'code': 'inpatient_examinations',
        'label': 'Исследования, проведённые в стационаре',
        'type': 'textarea'
    },
]

OPERATION_PROTOCOL_FIELDS = [
    {'code': 'operation_start', 'label': 'Дата и время начала операции', 'type': 'datetime-local'},
    {'code': 'operation_end', 'label': 'Дата и время окончания операции', 'type': 'datetime-local'},
    {'code': 'operation_name', 'label': 'Наименование оперативного вмешательства', 'type': 'textarea'},

    {'code': 'blood_group', 'label': 'Группа крови', 'type': 'select',
     'options': ['I', 'II', 'III', 'IV']},

    {'code': 'rh_factor', 'label': 'Rh-фактор', 'type': 'select',
     'options': ['Rh+', 'Rh-']},

    {'code': 'kell', 'label': 'KELL', 'type': 'select',
     'options': ['K+', 'K-']},

    {'code': 'rh_phenotype', 'label': 'Rh-фенотипирование', 'type': 'text'},

    {'code': 'diagnosis_main_icd', 'label': 'Основной диагноз (МКБ)', 'type': 'text'},
    {'code': 'diagnosis_main_text', 'label': 'Основной клинический диагноз', 'type': 'textarea'},

    {'code': 'diagnosis_complications_icd', 'label': 'Осложнения (МКБ)', 'type': 'text'},
    {'code': 'diagnosis_complications_text', 'label': 'Осложнения (клинически)', 'type': 'textarea'},

    {'code': 'diagnosis_secondary_icd', 'label': 'Сопутствующие заболевания (МКБ)', 'type': 'text'},
    {'code': 'diagnosis_secondary_text', 'label': 'Сопутствующие заболевания', 'type': 'textarea'},

    {'code': 'operating_room', 'label': 'Номер операционной', 'type': 'text'},
    {'code': 'used_materials', 'label': 'Использованные материалы', 'type': 'textarea'},

    {'code': 'anesthesia_used', 'label': 'Применённая анестезия', 'type': 'text'},
    {'code': 'blood_loss', 'label': 'Кровопотеря (мл)', 'type': 'number'},

    {'code': 'operation_outcome', 'label': 'Исход операции', 'type': 'textarea'},
]

DISCHARGE_EPICRISIS_FIELDS = [
    {
        'code': 'generated_summary',
        'label': 'Сводная информация (автоматически сформирована)',
        'type': 'readonly-textarea'
    },
    {
        'code': 'doctor_additions',
        'label': 'Дополнения врача',
        'type': 'textarea'
    }
]

FORMS_MAP = {
    'PRIMARY_VISIT': PRIMARY_VISIT_FIELDS,
    'HEAD_DOCTOR_REVIEW': HEAD_DOCTOR_REVIEW_FIELDS,
    'PREOPERATIVE_EPICRISIS': PREOPERATIVE_EPICRISIS_FIELDS,
    'OPERATION': OPERATION_PROTOCOL_FIELDS,
    'DISCHARGE_EPICRISIS': DISCHARGE_EPICRISIS_FIELDS,
}
