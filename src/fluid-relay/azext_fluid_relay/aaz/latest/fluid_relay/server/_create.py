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
    "fluid-relay server create",
)
class Create(AAZCommand):
    """Create a Fluid Relay server.

    :example: FluidRelayServer_Create
        az fluid-relay server create -n TestFluidRelay -l westus2 -g MyResourceGroup --sku standard --tags category=sales --identity type="SystemAssigned"
        az fluid-relay server create -n TestFluidRelay -l westus2 -g MyResourceGroup --sku standard --tags category=sales --identity type="SystemAssigned, UserAssigned" user-assigned-identities={"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/MyResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/id1","/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/MyResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/id2"}
    """

    _aaz_info = {
        "version": "2022-06-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.fluidrelay/fluidrelayservers/{}", "2022-06-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.server_name = AAZStrArg(
            options=["-n", "--name", "--server-name"],
            help="The Fluid Relay server resource name.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "CustomerManagedKeyEncryption"

        _args_schema = cls._args_schema
        _args_schema.key_identity = AAZObjectArg(
            options=["--key-identity"],
            arg_group="CustomerManagedKeyEncryption",
            help="All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.",
        )
        _args_schema.key_url = AAZStrArg(
            options=["--key-url"],
            arg_group="CustomerManagedKeyEncryption",
            help="key encryption key Url, with or without a version. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78 or https://contosovault.vault.azure.net/keys/contosokek. Key auto rotation is enabled by providing a key uri without version. Otherwise, customer is responsible for rotating the key. The keyEncryptionKeyIdentity(either SystemAssigned or UserAssigned) should have permission to access this key url.",
        )

        key_identity = cls._args_schema.key_identity
        key_identity.identity_type = AAZStrArg(
            options=["identity-type"],
            help="Values can be SystemAssigned or UserAssigned",
            enum={"SystemAssigned": "SystemAssigned", "UserAssigned": "UserAssigned"},
        )
        key_identity.user_assigned_identities = AAZStrArg(
            options=["user-assigned-identities"],
            help="user assigned identity to use for accessing key encryption key Url. Ex: /subscriptions/fa5fc227-a624-475e-b696-cdd604c735bc/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId. Mutually exclusive with identityType systemAssignedIdentity.",
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.provisioning_state = AAZStrArg(
            options=["--provisioning-state"],
            arg_group="Properties",
            help="Provision states for FluidRelay RP",
            enum={"Canceled": "Canceled", "Failed": "Failed", "Succeeded": "Succeeded"},
        )
        _args_schema.sku = AAZStrArg(
            options=["--sku"],
            arg_group="Properties",
            help="Sku of the storage associated with the resource",
            enum={"basic": "basic", "standard": "standard"},
        )

        # define Arg Group "Resource"

        _args_schema = cls._args_schema
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            arg_group="Resource",
            help="The type of identity used for the resource.",
        )
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Resource",
            help="The geo-location where the resource lives",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Resource",
            help="Resource tags.",
        )

        identity = cls._args_schema.identity
        identity.type = AAZStrArg(
            options=["type"],
            help="The identity type.",
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned, UserAssigned": "SystemAssigned, UserAssigned", "UserAssigned": "UserAssigned"},
        )
        identity.user_assigned_identities = AAZDictArg(
            options=["user-assigned-identities"],
            help="The list of user identities associated with the resource.",
        )

        user_assigned_identities = cls._args_schema.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            blank={},
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.FluidRelayServersCreateOrUpdate(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class FluidRelayServersCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.FluidRelay/fluidRelayServers/{fluidRelayServerName}",
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
                    "fluidRelayServerName", self.ctx.args.server_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroup", self.ctx.args.resource_group,
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
                    "api-version", "2022-06-01",
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
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("identity", AAZObjectType, ".identity")
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".type")
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("encryption", AAZObjectType)
                properties.set_prop("provisioningState", AAZStrType, ".provisioning_state")
                properties.set_prop("storagesku", AAZStrType, ".sku")

            encryption = _builder.get(".properties.encryption")
            if encryption is not None:
                encryption.set_prop("customerManagedKeyEncryption", AAZObjectType)

            customer_managed_key_encryption = _builder.get(".properties.encryption.customerManagedKeyEncryption")
            if customer_managed_key_encryption is not None:
                customer_managed_key_encryption.set_prop("keyEncryptionKeyIdentity", AAZObjectType, ".key_identity")
                customer_managed_key_encryption.set_prop("keyEncryptionKeyUrl", AAZStrType, ".key_url")

            key_encryption_key_identity = _builder.get(".properties.encryption.customerManagedKeyEncryption.keyEncryptionKeyIdentity")
            if key_encryption_key_identity is not None:
                key_encryption_key_identity.set_prop("identityType", AAZStrType, ".identity_type")
                key_encryption_key_identity.set_prop("userAssignedIdentityResourceId", AAZStrType, ".user_assigned_identities")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.identity = AAZObjectType()
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.encryption = AAZObjectType()
            properties.fluid_relay_endpoints = AAZObjectType(
                serialized_name="fluidRelayEndpoints",
                flags={"read_only": True},
            )
            properties.frs_tenant_id = AAZStrType(
                serialized_name="frsTenantId",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.storagesku = AAZStrType()

            encryption = cls._schema_on_200.properties.encryption
            encryption.customer_managed_key_encryption = AAZObjectType(
                serialized_name="customerManagedKeyEncryption",
            )

            customer_managed_key_encryption = cls._schema_on_200.properties.encryption.customer_managed_key_encryption
            customer_managed_key_encryption.key_encryption_key_identity = AAZObjectType(
                serialized_name="keyEncryptionKeyIdentity",
            )
            customer_managed_key_encryption.key_encryption_key_url = AAZStrType(
                serialized_name="keyEncryptionKeyUrl",
            )

            key_encryption_key_identity = cls._schema_on_200.properties.encryption.customer_managed_key_encryption.key_encryption_key_identity
            key_encryption_key_identity.identity_type = AAZStrType(
                serialized_name="identityType",
            )
            key_encryption_key_identity.user_assigned_identity_resource_id = AAZStrType(
                serialized_name="userAssignedIdentityResourceId",
            )

            fluid_relay_endpoints = cls._schema_on_200.properties.fluid_relay_endpoints
            fluid_relay_endpoints.orderer_endpoints = AAZListType(
                serialized_name="ordererEndpoints",
                flags={"read_only": True},
            )
            fluid_relay_endpoints.service_endpoints = AAZListType(
                serialized_name="serviceEndpoints",
                flags={"read_only": True},
            )
            fluid_relay_endpoints.storage_endpoints = AAZListType(
                serialized_name="storageEndpoints",
                flags={"read_only": True},
            )

            orderer_endpoints = cls._schema_on_200.properties.fluid_relay_endpoints.orderer_endpoints
            orderer_endpoints.Element = AAZStrType(
                flags={"read_only": True},
            )

            service_endpoints = cls._schema_on_200.properties.fluid_relay_endpoints.service_endpoints
            service_endpoints.Element = AAZStrType(
                flags={"read_only": True},
            )

            storage_endpoints = cls._schema_on_200.properties.fluid_relay_endpoints.storage_endpoints
            storage_endpoints.Element = AAZStrType(
                flags={"read_only": True},
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
                flags={"read_only": True},
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
                flags={"read_only": True},
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
                flags={"read_only": True},
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
                flags={"read_only": True},
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
                flags={"read_only": True},
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
                flags={"read_only": True},
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


__all__ = ["Create"]