# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RetryDrPlanExecutionDetails(object):
    """
    The details for retrying a failed group or step.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RetryDrPlanExecutionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param group_id:
            The value to assign to the group_id property of this RetryDrPlanExecutionDetails.
        :type group_id: str

        :param step_id:
            The value to assign to the step_id property of this RetryDrPlanExecutionDetails.
        :type step_id: str

        """
        self.swagger_types = {
            'group_id': 'str',
            'step_id': 'str'
        }

        self.attribute_map = {
            'group_id': 'groupId',
            'step_id': 'stepId'
        }

        self._group_id = None
        self._step_id = None

    @property
    def group_id(self):
        """
        **[Required]** Gets the group_id of this RetryDrPlanExecutionDetails.
        The unique id of the group to retry as a whole, or the group containing the step being retried.

        Example: `sgid1.group..examplegroupsgid`


        :return: The group_id of this RetryDrPlanExecutionDetails.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this RetryDrPlanExecutionDetails.
        The unique id of the group to retry as a whole, or the group containing the step being retried.

        Example: `sgid1.group..examplegroupsgid`


        :param group_id: The group_id of this RetryDrPlanExecutionDetails.
        :type: str
        """
        self._group_id = group_id

    @property
    def step_id(self):
        """
        Gets the step_id of this RetryDrPlanExecutionDetails.
        The unique id of the step to retry (optional). Only needed when retrying a step.

        Example: `sgid1.step..examplestepsgid`


        :return: The step_id of this RetryDrPlanExecutionDetails.
        :rtype: str
        """
        return self._step_id

    @step_id.setter
    def step_id(self, step_id):
        """
        Sets the step_id of this RetryDrPlanExecutionDetails.
        The unique id of the step to retry (optional). Only needed when retrying a step.

        Example: `sgid1.step..examplestepsgid`


        :param step_id: The step_id of this RetryDrPlanExecutionDetails.
        :type: str
        """
        self._step_id = step_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other