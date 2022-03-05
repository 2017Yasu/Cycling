# Cycling

## Tables

### CycleResults

| Name     | Type     |
| :------- | :------- |
| Date     | date     |
| Duration | Duration |
| Distance | float    |
| Average  | float    |
| Max      | float    |

### Cyclists

| Name       | Type   |
| :--------- | :----- |
| UserId (p) | string |
| Name       | string |
| TeamId     | string |
| Email      | Email  |

### Teams

| Name       | Type   |
| :--------- | :----- |
| TeamId (p) | string |
| Name       | string |
| LeaderId   | string |

## Command history

    django-admin startproject Cycling
    python manage.py startapp CRec
