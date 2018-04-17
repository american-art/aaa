# Item_Sheet1

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300026031`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300266038`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ObjectURI_
From column: _ItemID_
``` python
return "object/"+getValue("ItemID")
```

#### _GeneralFormat_Formatted_
From column: _GeneralFormat_
``` python
return getValue("GeneralFormat").capitalize()
```

#### _AAT_Type_
From column: _TypeURI_
``` python
return AATTerm.get_aat_term("aaa", getValue("GeneralFormat_Formatted"))
```

#### _TypeURI_
From column: _GeneralFormat_
``` python
return UM.uri_from_fields("thesauri/type/",getValue("AAT_Type"))
```

#### _AAT_TypeURI_
From column: _AAT_Type_
``` python
return AATTerm.get_aat_uri("aaa", getValue("GeneralFormat_Formatted"))
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

#### _SpecificFormat_Formatted_
From column: _SpecificFormat_
``` python
return getValue("SpecificFormat").capitalize()
```

#### _AAAT_FormatURI_
From column: _AAT_Format_
``` python
lookup = getValue('SpecificFormat_Formatted')
try:
    return AATTerm.get_aat_uri("aaa", lookup)
except:
    return ""
```

#### _AAT_Format_
From column: _FormatURI_
``` python
lookup = getValue("SpecificFormat_Formatted")
try:
    return AATTerm.get_aat_term("aaa", lookup)
except:
    return lookup
```

#### _FormatURI_
From column: _SpecificFormat_Formatted_
``` python
return UM.uri_from_fields("thesauri/format/", getValue("AAT_Format"))
```

#### _ClassificationURI_
From column: _AAT_Type_
``` python
if len(getValue("AAAT_FormatURI")):
    return UM.uri_from_fields("thesauri/classification/",getValue("AAT_Type"), getValue("AAT_Format"))
else:
    return UM.uri_from_fields("thesauri/classification/",getValue("AAT_Type"))
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


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AAAT_FormatURI_ | `uri` | `crm:E55_Type4`|
| _AAT_Type_ | `rdf:value` | `crm:E55_Type1`|
| _AAT_TypeURI_ | `uri` | `crm:E55_Type3`|
| _ClassificationURI_ | `uri` | `crm:E17_Type_Assignment1`|
| _FormatURI_ | `uri` | `crm:E55_Type2`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _TypeURI_ | `uri` | `crm:E55_Type1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E17_Type_Assignment1` | `crm:P101_had_as_general_use` | `crm:E55_Type3`|
| `crm:E17_Type_Assignment1` | `crm:P42_assigned` | `crm:E55_Type4`|
| `crm:E22_Man-Made_Object1` | `crm:P41i_was_classified_by` | `crm:E17_Type_Assignment1`|
| `crm:E22_Man-Made_Object1` | `crm:P2_has_type` | `crm:E55_Type2`|
| `crm:E22_Man-Made_Object1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E55_Type1` | `crm:P2i_is_type_of` | `crm:E22_Man-Made_Object1`|
| `crm:E55_Type1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300026031`|
| `crm:E55_Type2` | `crm:P2i_is_type_of` | `crm:E22_Man-Made_Object1`|
| `crm:E55_Type2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300266038`|
