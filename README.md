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
| Team       | Team   |
| Email      | Email  |

### Teams

| Name       | Type    |
| :--------- | :------ |
| TeamId (p) | string  |
| Name       | string  |
| Leader     | Cyclist |

## Command history

    django-admin startproject Cycling
    python manage.py startapp CRec
