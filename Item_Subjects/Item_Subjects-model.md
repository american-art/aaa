# Item_Subjects.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _ObjectURI_
From column: _ItemID_
``` python
return "object/"+getValue("ItemID")
```

#### _SubjectURI_
From column: _PersonID_
``` python
if getValue("PersonID"):
    return "person/"+getValue("PersonID")
elif getValue("InstitutionID"):
    return "institution/"+getValue("InstitutionID")
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _SubjectURI_ | `uri` | `crm:E39_Actor1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E22_Man-Made_Object1` | `crm:P62_depicts` | `crm:E39_Actor1`|
