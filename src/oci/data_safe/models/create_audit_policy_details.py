# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAuditPolicyDetails(object):
    """
    Details for the new audit policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAuditPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateAuditPolicyDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateAuditPolicyDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAuditPolicyDetails.
        :type compartment_id: str

        :param target_id:
            The value to assign to the target_id property of this CreateAuditPolicyDetails.
        :type target_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAuditPolicyDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAuditPolicyDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'target_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'target_id': 'targetId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._target_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateAuditPolicyDetails.
        The display name of the audit policy. The name does not have to be unique, and it is changeable.


        :return: The display_name of this CreateAuditPolicyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAuditPolicyDetails.
        The display name of the audit policy. The name does not have to be unique, and it is changeable.


        :param display_name: The display_name of this CreateAuditPolicyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateAuditPolicyDetails.
        The description of the audit policy.


        :return: The description of this CreateAuditPolicyDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateAuditPolicyDetails.
        The description of the audit policy.


        :param description: The description of this CreateAuditPolicyDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAuditPolicyDetails.
        The OCID of the compartment where you want to create the audit policy.


        :return: The compartment_id of this CreateAuditPolicyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAuditPolicyDetails.
        The OCID of the compartment where you want to create the audit policy.


        :param compartment_id: The compartment_id of this CreateAuditPolicyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this CreateAuditPolicyDetails.
        The OCID of the target for which the audit policy has to be created.


        :return: The target_id of this CreateAuditPolicyDetails.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this CreateAuditPolicyDetails.
        The OCID of the target for which the audit policy has to be created.


        :param target_id: The target_id of this CreateAuditPolicyDetails.
        :type: str
        """
        self._target_id = target_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAuditPolicyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateAuditPolicyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAuditPolicyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateAuditPolicyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAuditPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateAuditPolicyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAuditPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateAuditPolicyDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other