# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InternetGateway(object):
    """
    Represents a router that connects the edge of a VCN with the Internet. For an example scenario
    that uses an internet gateway, see
    `Typical Networking Service Scenarios`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/overview.htm#scenarios
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a InternetGateway.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a InternetGateway.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a InternetGateway.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a InternetGateway.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new InternetGateway object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this InternetGateway.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this InternetGateway.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this InternetGateway.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this InternetGateway.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this InternetGateway.
        :type id: str

        :param is_enabled:
            The value to assign to the is_enabled property of this InternetGateway.
        :type is_enabled: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this InternetGateway.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this InternetGateway.
        :type time_created: datetime

        :param vcn_id:
            The value to assign to the vcn_id property of this InternetGateway.
        :type vcn_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'is_enabled': 'bool',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'is_enabled': 'isEnabled',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._is_enabled = None
        self._lifecycle_state = None
        self._time_created = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this InternetGateway.
        The `OCID`__ of the compartment containing the internet gateway.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this InternetGateway.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this InternetGateway.
        The `OCID`__ of the compartment containing the internet gateway.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this InternetGateway.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this InternetGateway.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this InternetGateway.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this InternetGateway.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this InternetGateway.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this InternetGateway.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this InternetGateway.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InternetGateway.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this InternetGateway.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this InternetGateway.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this InternetGateway.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this InternetGateway.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this InternetGateway.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this InternetGateway.
        The internet gateway's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this InternetGateway.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InternetGateway.
        The internet gateway's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this InternetGateway.
        :type: str
        """
        self._id = id

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this InternetGateway.
        Whether the gateway is enabled. When the gateway is disabled, traffic is not
        routed to/from the Internet, regardless of route rules.


        :return: The is_enabled of this InternetGateway.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this InternetGateway.
        Whether the gateway is enabled. When the gateway is disabled, traffic is not
        routed to/from the Internet, regardless of route rules.


        :param is_enabled: The is_enabled of this InternetGateway.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this InternetGateway.
        The internet gateway's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"


        :return: The lifecycle_state of this InternetGateway.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this InternetGateway.
        The internet gateway's current state.


        :param lifecycle_state: The lifecycle_state of this InternetGateway.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this InternetGateway.
        The date and time the internet gateway was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this InternetGateway.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this InternetGateway.
        The date and time the internet gateway was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this InternetGateway.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this InternetGateway.
        The `OCID`__ of the VCN the Internet Gateway belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this InternetGateway.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this InternetGateway.
        The `OCID`__ of the VCN the Internet Gateway belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this InternetGateway.
        :type: str
        """
        self._vcn_id = vcn_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other