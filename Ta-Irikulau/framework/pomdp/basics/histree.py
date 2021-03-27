"""
This is a rather simple tree and tree node structure implementation to maintain belief history
"""

class HisTreeNode(object):
    def __init__(self, parent_node = None, action = None, observation = None, init_belief = None, layer = -1, index = -1):
        self._parent = parent_node
        if (action != None) and (observation != None):
            self._a_o = '{}-{}'.format(action.Name, observation.Name)  #in the format of "action-observation"
        else:
            self._a_o = '{}-{}'  #in the format of "action-observation"
        self._layer = layer  #-1 indicates uninitialized
        self._index = index  #-1 indicates uninitialized, where this index is counted from 0 to (max - 1) nodes in this layer
        self._belief = init_belief
        self._child_list_index = 0
        self._child_list = None
        self._immediate_reward_list = None  #The immediate reward list with respect to the belief state
        self._prob_o_s_a_list = None  #The probs list of making observation o, in state s, by action a
        self._immediate_reward = 0.0  #Stores the immediate reward = _immediate_reward_list * _belief
        self._current_reward = 0.0  #Stores the current accumulative reward
        self._name = '{}-{}-{}-{}'.format(self._a_o, self._layer, self._index, self._belief)

        if (parent_node != None):
            parent_node.AddChild(self)  #Add self to parent node's child list

    def __str__(self):
        return 'TreeNode({})'.format(self._name)

    def __repr__(self):
        return self._name

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, other):
        return (
            isinstance(other, HisTreeNode) and
            self.Name == other.Name
        )

    """
    To implement iterator for HisTreeNode's child list
    """
    def __iter__(self):
        return iter(self._child_list)

    def __next__(self):
        ret_val = None

        while self._child_list_index < len(self._child_list):
            ret_val = self._child_list[self._child_list_index]
            self._child_list_index += 1
            return ret_val
        else:
            self._child_list_index = 0
            raise StopIteration()

    def AddChild(self, node):
        if self._child_list == None:
            self._child_list = []

        self._child_list.append(node)

    def GetChildIndex(self, node):
        if self._child_list == None:
            return -1

        if len(self._child_list) == 0:
            return -1

        return self._child_list.index(node)

    """
    Properties
    """
    @property
    def Name(self):
        return self._name

    @property
    def Parent(self):
        return self._parent

    @property
    def ObservationByActionTag(self):
        return self._a_o

    @ObservationByActionTag.setter
    def ObservationByActionTag(self, value):
        self._a_o = value

    @property
    def Layer(self):
        return self._layer

    @property
    def Index(self):
        return self._index

    @property
    def Belief(self):
        return self._belief

    @Belief.setter
    def Belief(self, value):
        self._belief = value
        self._name = '{}-{}-{}-{}'.format(self._a_o, self._layer, self._index, self._belief)

    @property
    def ImmediateReward(self):
        return self._immediate_reward

    @ImmediateReward.setter
    def ImmediateReward(self, value):
        self._immediate_reward = value

    @property
    def ImmediateRewardData(self):
        return self._immediate_reward_list

    @ImmediateRewardData.setter
    def ImmediateRewardData(self, value):
        self._immediate_reward_list = value

    @property
    def Prob_o_s_a_Data(self):
        return self._prob_o_s_a_list

    @Prob_o_s_a_Data.setter
    def Prob_o_s_a_Data(self, value):
        self._prob_o_s_a_list = value

    @property
    def CurrentReward(self):
        return self._current_reward

    @CurrentReward.setter
    def CurrentReward(self, value):
        self._current_reward = value

    @property
    def ChildList(self):
        return self._child_list

"""
This is to keep track of the growth of the History Tree in dict manner, where i = 1:
"layer i":[list of HisTreeNode in this layer]
"layer i+1":[list of HisTreeNode in this layer]
...
"layer n":[list of HisTreeNode in this layer]
"""

class HisTree(object):
    def __init__(self):
        self._name = 'HisTree'
        self._HisTreeDictList = dict()

    def __str__(self):
        return 'HisTree({})'.format(self._name)

    def __repr__(self):
        return self._name

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, other):
        return (
            isinstance(other, HisTree) and
            self.Name == other.Name
        )

    def AddNodeInHistory(self, layer, histree_node):
        v_List = self._HisTreeDictList.get('layer-{}'.format(layer))

        if v_List == None:
            v_List = []
    
        v_List.append(histree_node)
        self._HisTreeDictList['layer-{}'.format(layer)] = v_List

    def GetHistoryByLayer(self, layer):
        v_List = self._HisTreeDictList.get('layer-{}'.format(layer))

        if v_List == None:
            v_List = []

        return v_List

    """
    Properties
    """
    @property
    def Name(self):
        return self._name