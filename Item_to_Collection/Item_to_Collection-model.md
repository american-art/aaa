# Item_to_Collection_Sheet1

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
| _CollectionURI_ | `uri` | `crm:E78_Collection1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E78_Collection1` | `crm:P46_is_composed_of` | `crm:E22_Man-Made_Object1`|
