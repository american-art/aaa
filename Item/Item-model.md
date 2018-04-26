# Item.csv

## Add Column
#### _Owner_Fixed_
From column: _Owner_
<br/>Value: `Archives of American Art`


## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300266036`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300080091`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/ulan/500269705`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300055547`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300055642`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300010358`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300312242`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ObjectURI_
From column: _ItemID_
``` python
return "object/"+getValue("ItemID")
```

#### _TitleURI_
From column: _Title_
``` python
return UM.uri_from_fields(getValue("ObjectURI")+"/title/",getValue("Title"))
```

#### _TitleLabel_
From column: _Title_
``` python
return getValue("Title")
```

#### _ProductionURI_
From column: _DisplayDate_
``` python
return getValue("ObjectURI")+"/production"
```

#### _DateBeginFormatted_
From column: _DateBegin_
``` python
if getValue("DateBegin"):
    if len(getValue("DateBegin"))==4:
        return getValue("DateBegin")+"-01-01"
    else:
        return getValue("DateBegin")
else:
    return ""
```

#### _DateEndFormatted_
From column: _DateEnd_
``` python
if getValue("DateEnd"):
    if len(getValue("DateEnd"))==4:
        return getValue("DateEnd")+"-01-01"
    else:
        return getValue("DateEnd")
else:
    return ""
```

#### _DescriptionURI_
From column: _Description_
``` python
if getValue("Description"):
    return getValue("ObjectURI")+"/description"
else:
    return ""
```

#### _UrlURI_
From column: _ResourceURL_
``` python
if getValue("ResourceURL"):
    return getValue("ResourceURL")
else:
    return ""
```

#### _LocationURI_
From column: _Current_Location_
``` python
if getValue("Current_Location"):
    return UM.uri_from_fields("thesauri/location/",getValue("Current_Location"))
else:
    return ""
```

#### _OwnerURI_
From column: _Owner_
``` python
return "http://data.aaa.si.edu"
```

#### _CreatorURI_
From column: _fkCreatorPersonID_
``` python
if getValue("fkCreatorPersonID"):
    return "person/"+getValue("fkCreatorPersonID")
elif getValue("fkCreatorInstitutionID"):
    return "institution/"+getValue("fkCreatorInstitutionID")
else:
    return ""
```

#### _InstitutionURI_
From column: _fkCreatorInstitutionID_
``` python
if getValue("fkCreatorInstitutionID"):
    return "institution/"+getValue("fkCreatorInstitutionID")
else:
    return ""
```

#### _RightURI_
From column: _RightsStatement_
``` python
if len(getValue("RightsStatement")):
    return UM.uri_from_fields("rights/",getValue("RightsStatement"))
else:
    return ""
```

#### _TimeSpanURI_
From column: _ProductionURI_
``` python
if getValue("DateBeginFormatted") or getValue("DateEndFormatted"):
    return getValue("ProductionURI")+"/timespan"
else:
    return ""
```

#### _FormsPartOfURI_
From column: _fkCollectionID_
``` python
return "object/"+getValue("ItemID") + "/formspartof"
```

#### _CollectionURI_
From column: _FormsPartOfURI_
``` python
return "collection/"+getValue("fkCollectionID")
```

#### _GeneralFormat_Formatted_
From column: _GeneralFormat_
``` python
return getValue("GeneralFormat").capitalize()
```

#### _ExtentStatement_
From column: _ExtentType_
``` python
return getValue("ExtentNum") + ' ' + getValue("ExtentType")
```

#### _ExtentURI_
From column: _ExtentStatement_
``` python
if len(getValue("ExtentStatement")):
    return "object/" + getValue("ItemID") + "/extent"
```

#### _CharacteristicURI_
From column: _PhysicalCharacteristic_
``` python
return UM.uri_from_fields("thesauri/characteristics/",getValue("PhysicalCharacteristic"))
```

#### _IdentifierURI_
From column: _ItemID_
``` python
return getValue("ObjectURI") + "/id"
```

#### _CoCreatorURI_
From column: _fkCoCreatorInstitutionID_
``` python
if getValue("fkCoCreatorPersonID"):
    return "person/"+getValue("fkCoCreatorPersonID")
elif getValue("fkCoCreatorInstitutionID"):
    return "institution/"+getValue("fkCoCreatorInstitutionID")
else:
    return ""
```

#### _SpecificFormat_Formatted_
From column: _SpecificFormat_
``` python
return getValue("SpecificFormat").capitalize()
```

#### _ExtentTypeURI_
From column: _ExtentType_
``` python
if len(getValue("ExtentType")):
    return UM.uri_from_fields("thesauri/extent/", getValue("ExtentType"))
else:
    return ""
```

#### _DimensionsLabel_
From column: _ItemSize_
``` python
if len(getValue("ItemSize")):
    return getValue("ItemSize")
elif len(getValue("DisplayDuration")):
    if len(getValue("ExactDuration")):
        return getValue("DisplayDuration") + " (" + getValue("ExactDuration") + ")"
    else:
        return getValue("DisplayDuration")
elif len(getValue("ExactDuration")):
    return getValue("ExactDuration")

return ""
```

#### _DimensionURI_
From column: _ItemSize_
``` python
if getValue("DimensionsLabel"):
    return getValue("ObjectURI")+"/dimensions"
else:
    return ""
```

#### _CitationURI_
From column: _Citation_
``` python
return getValue("ObjectURI") + "/citation"
```

#### _ArchivesURI_
From column: _OwnerURI_
``` python
return getValue("OwnerURI") + "/"
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ArchivesURI_ | `uri` | `crm:E40_Legal_Body1`|
| _CharacteristicURI_ | `uri` | `crm:E33_Linguistic_Object5`|
| _Citation_ | `rdf:value` | `crm:E33_Linguistic_Object7`|
| _CitationURI_ | `uri` | `crm:E33_Linguistic_Object7`|
| _CoCreatorURI_ | `uri` | `crm:E39_Actor2`|
| _CollectionURI_ | `uri` | `crm:E78_Collection1`|
| _CreatorURI_ | `uri` | `crm:E39_Actor1`|
| _Current_Location_ | `rdfs:label` | `crm:E53_Place1`|
| _DataDateStamp_ | `dc:date` | `crm:E42_Identifier1`|
| _DateBeginFormatted_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _DateEndFormatted_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _Description_ | `rdf:value` | `crm:E33_Linguistic_Object2`|
| _DescriptionURI_ | `uri` | `crm:E33_Linguistic_Object2`|
| _DimensionURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _DimensionsLabel_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _DisplayDate_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _ExtentStatement_ | `rdf:value` | `crm:E33_Linguistic_Object4`|
| _ExtentType_ | `crm:P2_has_type` | `crm:E33_Linguistic_Object4`|
| _ExtentURI_ | `uri` | `crm:E33_Linguistic_Object4`|
| _IdentifierURI_ | `uri` | `crm:E42_Identifier1`|
| _ItemID_ | `rdf:value` | `crm:E42_Identifier1`|
| _LocationURI_ | `uri` | `crm:E53_Place1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _Owner_Fixed_ | `rdfs:label` | `crm:E40_Legal_Body1`|
| _PhysicalCharacteristic_ | `rdf:value` | `crm:E33_Linguistic_Object5`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|
| _ResourceURL_ | `rdfs:label` | `foaf:Document1`|
| _RightURI_ | `uri` | `crm:E33_Linguistic_Object3`|
| _RightsStatement_ | `rdf:value` | `crm:E33_Linguistic_Object3`|
| _TimeSpanURI_ | `uri` | `crm:E52_Time-Span1`|
| _Title_ | `rdfs:label` | `crm:E35_Title1`|
| _Title_ | `rdf:value` | `crm:E35_Title1`|
| _TitleLabel_ | `rdfs:label` | `crm:E22_Man-Made_Object1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|
| _UrlURI_ | `uri` | `foaf:Document1`|
| _has_representation_ | `uri` | `crm:E38_Image1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P14_carried_out_by` | `crm:E39_Actor1`|
| `crm:E12_Production1` | `crm:P14_carried_out_by` | `crm:E39_Actor2`|
| `crm:E12_Production1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P129i_is_subject_of` | `crm:E33_Linguistic_Object2`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object3`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object4`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object5`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object7`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E22_Man-Made_Object1` | `foaf:depiction` | `crm:E38_Image1`|
| `crm:E22_Man-Made_Object1` | `crm:P52_has_current_owner` | `crm:E40_Legal_Body1`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E22_Man-Made_Object1` | `crm:P55_has_current_location` | `crm:E53_Place1`|
| `crm:E22_Man-Made_Object1` | `crm:P46i_forms_part_of` | `crm:E78_Collection1`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300266036`|
| `crm:E33_Linguistic_Object2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E33_Linguistic_Object2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300080091`|
| `crm:E33_Linguistic_Object3` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300055547`|
| `crm:E33_Linguistic_Object4` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300055642`|
| `crm:E33_Linguistic_Object5` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300010358`|
| `crm:E35_Title1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E40_Legal_Body1` | `skos:exactMatch` | `http://vocab.getty.edu/ulan/500269705`|
| `crm:E40_Legal_Body1` | `skos:exactMatch` | `http://vocab.getty.edu/ulan/500269705`|
| `crm:E40_Legal_Body1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300312242`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
