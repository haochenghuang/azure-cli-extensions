# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "voice-service gateway update",
)
class Update(AAZCommand):
    """Update a communications gateway

    :example: Update a gateway
        az voice-service gateway update -n gateway-name -g rg --tags "{tag:test,tag2:test2}"
    """

    _aaz_info = {
        "version": "2023-01-31",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.voiceservices/communicationsgateways/{}", "2023-01-31"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.gateway_name = AAZStrArg(
            options=["-n", "--name", "--gateway-name"],
            help="Unique identifier for this deployment",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,24}$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Resource"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Resource",
            help="Resource tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.CommunicationsGatewaysGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.CommunicationsGatewaysCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class CommunicationsGatewaysGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VoiceServices/communicationsGateways/{communicationsGatewayName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "communicationsGatewayName", self.ctx.args.gateway_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-01-31",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_communications_gateway_read(cls._schema_on_200)

            return cls._schema_on_200

    class CommunicationsGatewaysCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VoiceServices/communicationsGateways/{communicationsGatewayName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "communicationsGatewayName", self.ctx.args.gateway_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-01-31",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_communications_gateway_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("tags", AAZDictType, ".tags")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_communications_gateway_read = None

    @classmethod
    def _build_schema_communications_gateway_read(cls, _schema):
        if cls._schema_communications_gateway_read is not None:
            _schema.id = cls._schema_communications_gateway_read.id
            _schema.location = cls._schema_communications_gateway_read.location
            _schema.name = cls._schema_communications_gateway_read.name
            _schema.properties = cls._schema_communications_gateway_read.properties
            _schema.system_data = cls._schema_communications_gateway_read.system_data
            _schema.tags = cls._schema_communications_gateway_read.tags
            _schema.type = cls._schema_communications_gateway_read.type
            return

        cls._schema_communications_gateway_read = _schema_communications_gateway_read = AAZObjectType()

        communications_gateway_read = _schema_communications_gateway_read
        communications_gateway_read.id = AAZStrType(
            flags={"read_only": True},
        )
        communications_gateway_read.location = AAZStrType(
            flags={"required": True},
        )
        communications_gateway_read.name = AAZStrType(
            flags={"read_only": True},
        )
        communications_gateway_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        communications_gateway_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        communications_gateway_read.tags = AAZDictType()
        communications_gateway_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_communications_gateway_read.properties
        properties.auto_generated_domain_name_label = AAZStrType(
            serialized_name="autoGeneratedDomainNameLabel",
            flags={"read_only": True},
        )
        properties.auto_generated_domain_name_label_scope = AAZStrType(
            serialized_name="autoGeneratedDomainNameLabelScope",
        )
        properties.codecs = AAZListType(
            flags={"required": True},
        )
        properties.connectivity = AAZStrType(
            flags={"required": True},
        )
        properties.e911_type = AAZStrType(
            serialized_name="e911Type",
            flags={"required": True},
        )
        properties.emergency_dial_strings = AAZListType(
            serialized_name="emergencyDialStrings",
        )
        properties.on_prem_mcp_enabled = AAZBoolType(
            serialized_name="onPremMcpEnabled",
        )
        properties.platforms = AAZListType(
            flags={"required": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.service_locations = AAZListType(
            serialized_name="serviceLocations",
            flags={"required": True},
        )
        properties.status = AAZStrType()
        properties.teams_voicemail_pilot_number = AAZStrType(
            serialized_name="teamsVoicemailPilotNumber",
        )

        codecs = _schema_communications_gateway_read.properties.codecs
        codecs.Element = AAZStrType()

        emergency_dial_strings = _schema_communications_gateway_read.properties.emergency_dial_strings
        emergency_dial_strings.Element = AAZStrType()

        platforms = _schema_communications_gateway_read.properties.platforms
        platforms.Element = AAZStrType()

        service_locations = _schema_communications_gateway_read.properties.service_locations
        service_locations.Element = AAZObjectType()

        _element = _schema_communications_gateway_read.properties.service_locations.Element
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.primary_region_properties = AAZObjectType(
            serialized_name="primaryRegionProperties",
            flags={"required": True},
        )

        primary_region_properties = _schema_communications_gateway_read.properties.service_locations.Element.primary_region_properties
        primary_region_properties.allowed_media_source_address_prefixes = AAZListType(
            serialized_name="allowedMediaSourceAddressPrefixes",
        )
        primary_region_properties.allowed_signaling_source_address_prefixes = AAZListType(
            serialized_name="allowedSignalingSourceAddressPrefixes",
        )
        primary_region_properties.esrp_addresses = AAZListType(
            serialized_name="esrpAddresses",
        )
        primary_region_properties.operator_addresses = AAZListType(
            serialized_name="operatorAddresses",
            flags={"required": True},
        )

        allowed_media_source_address_prefixes = _schema_communications_gateway_read.properties.service_locations.Element.primary_region_properties.allowed_media_source_address_prefixes
        allowed_media_source_address_prefixes.Element = AAZStrType()

        allowed_signaling_source_address_prefixes = _schema_communications_gateway_read.properties.service_locations.Element.primary_region_properties.allowed_signaling_source_address_prefixes
        allowed_signaling_source_address_prefixes.Element = AAZStrType()

        esrp_addresses = _schema_communications_gateway_read.properties.service_locations.Element.primary_region_properties.esrp_addresses
        esrp_addresses.Element = AAZStrType()

        operator_addresses = _schema_communications_gateway_read.properties.service_locations.Element.primary_region_properties.operator_addresses
        operator_addresses.Element = AAZStrType()

        system_data = _schema_communications_gateway_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        tags = _schema_communications_gateway_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_communications_gateway_read.id
        _schema.location = cls._schema_communications_gateway_read.location
        _schema.name = cls._schema_communications_gateway_read.name
        _schema.properties = cls._schema_communications_gateway_read.properties
        _schema.system_data = cls._schema_communications_gateway_read.system_data
        _schema.tags = cls._schema_communications_gateway_read.tags
        _schema.type = cls._schema_communications_gateway_read.type


__all__ = ["Update"]