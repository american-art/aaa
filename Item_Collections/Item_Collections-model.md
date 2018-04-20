# Item_Collections_Sheet1

## Add Column
#### _Owner_
From column: _CollectionURI_
<br/>Value: `Archives of American Art`

#### _OwnerURI_
From column: _Owner_
<br/>Value: `http://data.aaa.si.edu/`


## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300055642`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _CollectionURI_
From column: _IdentifierURI_
``` python
return "collection/" + getValue("COLLECTIONID")
```

#### _IdentifierURI_
From column: _COLLECTIONID_
``` python
return getValue("CollectionURI") + "/id"
```

#### _CodeURI_
From column: _COLLCODE_
``` python
return getValue("CollectionURI") + "/code"
```

#### _TitleURI_
From column: _COLLECTIONTITLE_
``` python
return UM.uri_from_fields(getValue("CollectionURI")+"/title/",getValue("COLLECTIONTITLE"))
```

#### _CreatorURI_
From column: _FKCREATOREVENTID_
``` python
if len(getValue("FKCREATORPERSONID")):
    uri = "person/" + getValue("FKCREATORPERSONID")
elif len(getValue("FKCREATORINSTITUTIONID")):
    uri = "institution/" + getValue("FKCREATORINSTITUTIONID")
elif len(getValue("FKCREATOREVENTID")):
    uri = "event/" + getValue("FKCREATOREVENTID")

return uri
```

#### _CoCreatorURL_
From column: _FKCOCREATOREVENTID_
``` python
if len(getValue("FKCOCREATORPERSONID")):
    uri = "person/" + getValue("FKCOCREATORPERSONID")
elif len(getValue("FKCOCREATORINSTITUTIONID")):
    uri = "institution/" + getValue("FKCOCREATORINSTITUTIONID")
elif len(getValue("FKCOCREATOREVENTID")):
    uri = "event/" + getValue("FKCOCREATOREVENTID")

return uri
```

#### _CollectionURL_Label_
From column: _COLLECTIONURL_
``` python
return getValue("COLLECTIONURL")
```

#### _AAT_Medium_
From column: _MEDIUM_
``` python
medium = getValue("MEDIUM")
if medium == "personal papers":
    return "http://vocab.getty.edu/aat/300028037"
else:
    return "http://vocab.getty.edu/aat/300027772"
```

#### _DATEBEGIN_
From column: _DATEBEGIN_
``` python

```

#### _DATEEND_
From column: _DATEEND_
``` python

```

#### _ExtentURI_
From column: _EXTENT_
``` python
return getValue("CollectionURI") + "/extent"
```

#### _ProductionURI_
From column: _TitleURI_
``` python
return getValue("CollectionURI") + "/production"
```

#### _CollectionLabel_
From column: _COLLECTIONTITLE_
``` python
date = getValue("DISPLAYDATE") or "undated"
return getValue("COLLECTIONTITLE")+ ", " + date

```

#### _TimeSpanURI_
From column: _ProductionURI_
``` python
return getValue("ProductionURI") + "/timespan"
```

#### _DateBeginFormatted_
From column: _DATEBEGIN_
``` python
if len(getValue('DATEBEGIN')) >= 4:
    return getValue("DATEBEGIN")[:4]
```

#### _DateEndFormatted_
From column: _DATEEND_
``` python
if len(getValue('DATEEND')) >= 4:
    return getValue("DATEEND")[:4]
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AAT_Medium_ | `uri` | `crm:E55_Type1`|
| _COLLCODE_ | `rdfs:label` | `crm:E42_Identifier1`|
| _COLLECTIONTITLE_ | `rdfs:label` | `crm:E35_Title1`|
| _COLLECTIONTITLE_ | `rdf:value` | `crm:E35_Title1`|
| _COLLECTIONURL_ | `uri` | `foaf:Document1`|
| _CoCreatorURL_ | `uri` | `crm:E39_Actor2`|
| _CodeURI_ | `uri` | `crm:E42_Identifier1`|
| _CollectionLabel_ | `rdfs:label` | `crm:E78_Collection1`|
| _CollectionURI_ | `uri` | `crm:E78_Collection1`|
| _CreatorURI_ | `uri` | `crm:E39_Actor1`|
| _DateBeginFormatted_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _DateEndFormatted_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _EXTENT_ | `rdf:value` | `crm:E33_Linguistic_Object2`|
| _ExtentURI_ | `uri` | `crm:E33_Linguistic_Object2`|
| _Owner_ | `rdfs:label` | `crm:E40_Legal_Body1`|
| _OwnerURI_ | `uri` | `crm:E40_Legal_Body1`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|
| _TimeSpanURI_ | `uri` | `crm:E52_Time-Span1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P14_carried_out_by` | `crm:E39_Actor1`|
| `crm:E12_Production1` | `crm:P14_carried_out_by` | `crm:E39_Actor2`|
| `crm:E12_Production1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E33_Linguistic_Object2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300055642`|
| `crm:E33_Linguistic_Object2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300055642`|
| `crm:E40_Legal_Body1` | `crm:P52i_is_current_owner_of` | `crm:E78_Collection1`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E78_Collection1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E78_Collection1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object2`|
| `crm:E78_Collection1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E78_Collection1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E78_Collection1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E78_Collection1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E78_Collection1` | `crm:P52_has_current_owner` | `crm:E40_Legal_Body1`|
