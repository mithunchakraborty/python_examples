from ...mailings.models import *
from ...mailings.services.mailchimp import add_mailchimp_with_tag
from ...cases.models import Case
from typing import Union

def add_email_to_common_mailchimp_list(email: str):
    """
    Добавляет email в общий лист рассылки
    """
    add_mailchimp_with_tag(
        audience_name='COMMON',
        email=email,
        tag='COMMON TAG'
    )

    CommonMailingList.objects.get_or_create(email=email)


def add_email_to_case_mailchimp_list(email: str, case_id: Union[int, str]):
    """
    Добавляет email в лист рассылки по делу
    """
    case = Case.objects.get(pk=case_id)

    add_mailchimp_with_tag(
        audience_name='CASES',
        email=email,
        tag=f'Case {case.name}'
    )

    CaseMailingList.objects.get_or_create(email=email, case=case)
