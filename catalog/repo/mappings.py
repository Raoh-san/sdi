

MD_CORE_MODEL = {
    'typename': 'pycsw:CoreMetadata',
    'outputschema': 'http://pycsw.org/metadata',
    'mappings': {
        'pycsw:Identifier': 'uuid',
        'pycsw:Typename': 'csw_typename',
        'pycsw:Schema': 'csw_schema',
        'pycsw:MdSource': 'csw_mdsource',
        'pycsw:InsertDate': 'csw_insert_date',
        'pycsw:XML': 'metadata_xml',
        'pycsw:AnyText': 'csw_anytext',
        'pycsw:Language': 'language',
        'pycsw:Title': 'title',
        'pycsw:Abstract': 'abstract',
        'pycsw:Keywords': 'keyword_csv',
        'pycsw:KeywordType': 'keywordstype',
        'pycsw:Format': 'spatial_representation_type_string',
        'pycsw:Source': 'source',
        'pycsw:Date': 'date',
        'pycsw:Modified': 'date',
        'pycsw:Type': 'csw_type',
        'pycsw:BoundingBox': 'csw_wkt_geometry',
        'pycsw:CRS': 'crs',
        'pycsw:AlternateTitle': 'alternate',
        'pycsw:RevisionDate': 'date',
        'pycsw:CreationDate': 'date',
        'pycsw:PublicationDate': 'date',
        'pycsw:OrganizationName': 'uuid',
        'pycsw:SecurityConstraints': 'securityconstraints',
        'pycsw:ParentIdentifier': 'parentidentifier',
        'pycsw:TopicCategory': 'topiccategory',
        'pycsw:ResourceLanguage': 'resourcelanguage',
        'pycsw:GeographicDescriptionCode': 'geodescode',
        'pycsw:Denominator': 'denominator',
        'pycsw:DistanceValue': 'distancevalue',
        'pycsw:DistanceUOM': 'distanceuom',
        'pycsw:TempExtent_begin': 'temporal_extent_start',
        'pycsw:TempExtent_end': 'temporal_extent_end',
        'pycsw:ServiceType': 'servicetype',
        'pycsw:ServiceTypeVersion': 'servicetypeversion',
        'pycsw:Operation': 'operation',
        'pycsw:CouplingType': 'couplingtype',
        'pycsw:OperatesOn': 'operateson',
        'pycsw:OperatesOnIdentifier': 'operatesonidentifier',
        'pycsw:OperatesOnName': 'operatesoname',
        'pycsw:Degree': 'degree',
        'pycsw:AccessConstraints': 'accessconstraints',
        'pycsw:OtherConstraints': 'otherconstraints',
        'pycsw:Classification': 'classification',
        'pycsw:ConditionApplyingToAccessAndUse': 'conditionapplyingtoaccessanduse',
        'pycsw:Lineage': 'lineage',
        'pycsw:ResponsiblePartyRole': 'responsiblepartyrole',
        'pycsw:SpecificationTitle': 'specificationtitle',
        'pycsw:SpecificationDate': 'specificationdate',
        'pycsw:SpecificationDateType': 'specificationdatetype',
        'pycsw:Creator': 'creator',
        'pycsw:Publisher': 'publisher',
        'pycsw:Contributor': 'contributor',
        'pycsw:Relation': 'relation',
        'pycsw:Links': 'download_links',
    }
}
