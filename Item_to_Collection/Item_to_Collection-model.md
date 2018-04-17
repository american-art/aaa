# Item_to_Collection.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _ObjectURI_
From column: _ItemID_
``` python
return 'object/' + getValue("ItemID")
```

#### _CollectionURI_
From column: _fkCollectionID_
``` python
return 'collection/' + getValue("fkCollectionID")
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _fkCollectionID_ | `uri` | `crm:E78_Collection1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E22_Man-Made_Object1` | `crm:P46i_forms_part_of` | `crm:E78_Collection1`|
