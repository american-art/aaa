# Item_People.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404651`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404652`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404672`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ConstituentURI_
From column: _PERSONID_
``` python
return "person/"+getValue("PERSONID")
```

#### _PrefIdURI_
From column: _PERSONID_
``` python
return getValue("ConstituentURI")+"/pref_id"
```

#### _IdLabel_
From column: _PERSONID_
``` python
return getValue("PERSONID")
```

#### _NameLabel_
From column: _DISPLAYNAME_
``` python
return getValue("DISPLAYNAME")
```

#### _NameURI_
From column: _DISPLAYNAME_
``` python
if getValue("DISPLAYNAME"):
    return getValue("ConstituentURI")+"/name"
else:
    return ""
```

#### _NameLabel1_
From column: _NameURI_
``` python
return getValue("DISPLAYNAME")
```

#### _FirstNameURI_
From column: _PERSONFNAME_
``` python
if getValue("PERSONFNAME"):
    return getValue("ConstituentURI")+"/first_name"
else:
    return ""
```

#### _FirstNameTypeURI_
From column: _FirstNameURI_
``` python
if getValue("PERSONFNAME"):
    return "thesauri/name_type/first_name"
else:
    return ""
```

#### _LastNameURI_
From column: _PERSONLNAME_
``` python
if getValue("PERSONLNAME"):
    return getValue("ConstituentURI")+"/last_name"
else:
    return ""
```

#### _LastNameTypeURI_
From column: _LastNameURI_
``` python
if getValue("PERSONLNAME"):
    return "thesauri/name_type/last_name"
else:
    return ""
```

#### _SortNameURI_
From column: _IDENTIFIER_
``` python
if getValue("IDENTIFIER"):
    return getValue("ConstituentURI")+"/sort_name"
else:
    return ""
```

#### _BirthURI_
From column: _BORNPLACE_
``` python
if getValue("BORNPLACE") or getValue("DISPLAYDATEBORN"):
    return getValue("ConstituentURI")+"/birth"
else:
    return ""
```

#### _BirthDateURI_
From column: _DISPLAYDATEBORN_
``` python
if getValue("DISPLAYDATEBORN"):
    return getValue("BirthURI")+"/timespan"
else:
    return ""
```

#### _BirthDateEarliest_
From column: _DISPLAYDATEBORN_
``` python
if getValue("DISPLAYDATEBORN") and len(getValue("DISPLAYDATEBORN")) == 4:
        return getValue("DISPLAYDATEBORN")+"-01-01"
else:
    return ""
```

#### _BirthDateLatest_
From column: _BirthDateEarliest_
``` python
if getValue("DISPLAYDATEBORN") and len(getValue("DISPLAYDATEBORN")) == 4:
        return getValue("DISPLAYDATEBORN")+"-12-31"
else:
    return ""
```

#### _DeathURI_
From column: _DISPLAYDATEDIED_
``` python
if getValue("DIEDPLACE") or getValue("DISPLAYDATEDIED"):
    return getValue("ConstituentURI")+"/death"
else:
    return ""
```

#### _DeathDateURI_
From column: _DISPLAYDATEDIED_
``` python
if getValue("DISPLAYDATEDIED"):
    return getValue("DeathURI")+"/timespan"
else:
    return ""
```

#### _DeathDateEarliest_
From column: _DISPLAYDATEDIED_
``` python
if getValue("DISPLAYDATEDIED") and len(getValue("DISPLAYDATEDIED")) == 4:
        return getValue("DISPLAYDATEDIED")+"-01-01"
else:
    return ""
```

#### _DeathDateLatest_
From column: _DeathDateEarliest_
``` python
if getValue("DISPLAYDATEDIED") and len(getValue("DISPLAYDATEDIED")) == 4:
        return getValue("DISPLAYDATEDIED")+"-12-31"
else:
    return ""
```

#### _BirthPlaceURI_
From column: _BORNPLACE_
``` python
if getValue("BORNPLACE"):
    return UM.uri_from_fields("thesauri/location/",getValue("BORNPLACE"))
else:
    return ""
```

#### _DIEDPLACE_
From column: _DIEDPLACE_
``` python
if getValue("DIEDPLACE"):
    return UM.uri_from_fields("thesauri/location/",getValue("DIEDPLACE"))
else:
    return ""
```

#### _DeathPlaceURI_
From column: _DIEDPLACE_
``` python
if getValue("DIEDPLACE"):
    return UM.uri_from_fields("thesauri/location/",getValue("DIEDPLACE"))
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _BORNPLACE_ | `rdfs:label` | `crm:E53_Place1`|
| _BirthDateEarliest_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _BirthDateLatest_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _BirthDateURI_ | `uri` | `crm:E52_Time-Span1`|
| _BirthPlaceURI_ | `uri` | `crm:E53_Place1`|
| _BirthURI_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _ConstituentURI_ | `uri` | `crm:E39_Actor1`|
| _DIEDPLACE_ | `rdfs:label` | `crm:E53_Place2`|
| _DISPLAYDATEBORN_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _DISPLAYDATEDIED_ | `rdfs:label` | `crm:E52_Time-Span2`|
| _DISPLAYNAME_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _DeathDateEarliest_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span2`|
| _DeathDateLatest_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span2`|
| _DeathDateURI_ | `uri` | `crm:E52_Time-Span2`|
| _DeathPlaceURI_ | `uri` | `crm:E53_Place2`|
| _DeathURI_ | `uri` | `crm:E64_End_of_Existence1`|
| _FirstNameTypeURI_ | `uri` | `crm:E55_Type1`|
| _FirstNameURI_ | `uri` | `crm:E82_Actor_Appellation2`|
| _IDENTIFIER_ | `rdf:value` | `crm:E82_Actor_Appellation4`|
| _IdLabel_ | `rdfs:label` | `crm:E42_Identifier1`|
| _LastNameTypeURI_ | `uri` | `crm:E55_Type2`|
| _LastNameURI_ | `uri` | `crm:E82_Actor_Appellation3`|
| _NameLabel_ | `rdfs:label` | `crm:E39_Actor1`|
| _NameLabel1_ | `rdfs:label` | `crm:E82_Actor_Appellation1`|
| _NameURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _PERSONFNAME_ | `rdf:value` | `crm:E82_Actor_Appellation2`|
| _PERSONID_ | `rdf:value` | `crm:E42_Identifier1`|
| _PERSONLNAME_ | `rdf:value` | `crm:E82_Actor_Appellation3`|
| _PrefIdURI_ | `uri` | `crm:E42_Identifier1`|
| _SortNameURI_ | `uri` | `crm:E82_Actor_Appellation4`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation4`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E55_Type1` | `skos:broadMatch` | `http://vocab.getty.edu/aat/300404651`|
| `crm:E55_Type2` | `skos:broadMatch` | `http://vocab.getty.edu/aat/300404652`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E63_Beginning_of_Existence1` | `crm:P7_took_place_at` | `crm:E53_Place1`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
| `crm:E64_End_of_Existence1` | `crm:P7_took_place_at` | `crm:E53_Place2`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation2`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation3`|
| `crm:E82_Actor_Appellation1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E82_Actor_Appellation2` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E82_Actor_Appellation3` | `crm:P2_has_type` | `crm:E55_Type2`|
| `crm:E82_Actor_Appellation4` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404672`|
