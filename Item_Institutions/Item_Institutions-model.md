# Item_Institutions.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ConstituentURI_
From column: _INSTITUTIONID_
``` python
return "institution/"+getValue("INSTITUTIONID")
```

#### _PrefIdURI_
From column: _INSTITUTIONID_
``` python
return getValue("ConstituentURI")+"/pref_id"
```

#### _IdLabel_
From column: _INSTITUTIONID_
``` python
return getValue("INSTITUTIONID")
```

#### _NameURI_
From column: _ConstituentURI_
``` python
return getValue("ConstituentURI")+"/name"
```

#### _NameLabel_
From column: _INSTITUTIONNAME_
``` python
return getValue("INSTITUTIONNAME")
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ConstituentURI_ | `uri` | `crm:E39_Actor1`|
| _INSTITUTIONID_ | `rdf:value` | `crm:E42_Identifier1`|
| _INSTITUTIONNAME_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _IdLabel_ | `rdfs:label` | `crm:E42_Identifier1`|
| _NameLabel_ | `rdfs:label` | `crm:E39_Actor1`|
| _NameURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _PrefIdURI_ | `uri` | `crm:E42_Identifier1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E82_Actor_Appellation1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
