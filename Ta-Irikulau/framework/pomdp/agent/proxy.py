from framework.pomdp.basics.histree import HisTreeNode
from framework.pomdp.basics.histree import HisTree
import numpy as np

"""
The design/implementation of the agent in POMDP world
"""

class Agent(object):
    def __init__(self):
        self._transition_model = None
        self._observation_model = None
        self._reward_model = None
        self._horizon_length = -1
        self._discount_factor = 1
        self._root_node = None
        self._histree = None
        self._logger = None

    def Configure(self, T, O, R, horizon_length, discount_factor):
        self._transition_model = T
        self._observation_model = O
        self._reward_model = R
        self._horizon_length = horizon_length
        self._discount_factor = discount_factor

    def Inflate(self, root_node, histree, logger):
        self._root_node = root_node
        self._histree = histree
        self._logger = logger

        self._logger.Info('Agent initialization...')

    """
    Calculate the immediate reward with regard to the updated belief by means of probabilistic simulation
    """
    def CalculateImmediateReward(self, updated_belief, a, s_list, o_list):
        simulated_prob_ary = np.array(updated_belief) #the very initial is the same as belief state
        b_equal_distributed = False
        immediate_reward = [-1 for _ in updated_belief]
        simulated_prob = [0 for _ in updated_belief]
        ret_dict = {}

        """
        I think after the very initial rigid defined version, I should try to express action/state/observation
        in terms of factors(maybe human readerable), that's the topology of expresion, possibly the Bayesian!!
        to be conti...
        """

        if a.Name == 'Listen':
            #I think we should return in according to reward model...to be conti
            for i in range(len(updated_belief)):
                simulated_prob_ary[i] = np.random.random()
                simulated_prob[i] = simulated_prob_ary[i]                

            simulated_prob = self.NormalizeProbability(simulated_prob)

            self._logger.Info('    A({}): immediate reward = {}'.format(a.Name, immediate_reward))
            self._logger.Info('        simulated probs = {}'.format(simulated_prob))

            ret_dict['immediate_reward'] = immediate_reward  #directly return -1 as immediate return
            ret_dict['simulated_prob'] = simulated_prob

            return ret_dict
        elif (a.Name == 'Open_Left') or (a.Name == 'Open_Right'):
            #Need to simulate tiger position by random with regards to updated_belief
            #I think we should simulate according to the given b(s) interval for all s of belief state
            if ((np.max(simulated_prob_ary) - np.min(simulated_prob_ary)) < 1e-2) or (np.max(simulated_prob_ary) == np.min(simulated_prob_ary)):
                b_equal_distributed = True  #if the (max - min < 0.01) or (max == min), treat all belief state equal probabilistically distributed

            for i in range(len(updated_belief)):
                simulated_prob_ary[i] = np.random.random()
                simulated_prob[i] = simulated_prob_ary[i]

            simulated_prob = self.NormalizeProbability(simulated_prob)

            """
            if (b_equal_distributed == True):
                #np.random.seed(len(updated_belief))  #It doesn't meets the requirement

                for i in range(len(updated_belief)):
                    simulated_prob_ary[i] = np.random.random()
            else:
                #Randomize in distinct interval for each state
                for i in range(len(updated_belief)):
                    simulated_prob_ary[i] = np.random.choice(updated_belief[i], size = 1)
            """

            #Get the index of the maximum in simulated_prob_ary
            index_max_simulated_prob_ary = np.argmax(simulated_prob_ary) #ignore the case that there might exists euqal probability

            immediate_reward[index_max_simulated_prob_ary] = self._reward_model.GetRwrardByActionStateObservation(
                                                                                    o_list[index_max_simulated_prob_ary],
                                                                                    s_list[index_max_simulated_prob_ary],
                                                                                    a)

            for i in range(len(immediate_reward)):
                if i != index_max_simulated_prob_ary:
                    immediate_reward[i] = self._reward_model.GetRwrardByActionStateObservation(
                                                                 o_list[i],
                                                                 s_list[i],
                                                                 a)

            self._logger.Info('    A({}): immediate reward = {}'.format(a.Name, immediate_reward))
            self._logger.Debug('        equal distributed = {}'.format(b_equal_distributed))
            self._logger.Info('        simulated probs = {}, max index = {}'.format(simulated_prob, index_max_simulated_prob_ary))

            ret_dict['immediate_reward'] = immediate_reward
            ret_dict['simulated_prob'] = simulated_prob

            return ret_dict

    """
    Calculate the accumulative rewards for distinct HisTreeNode in each layer of the simulated HisTree.
    We are using bottom up style.
    """
    def CalculateSimulationReward(self):
        #Figure out the list containing the layer from bottom to the top
        layer_bottom_up = [layer for layer in range(self._horizon_length)]
        layer_bottom_up.reverse()

        self._logger.Info('------------------------------------')
        self._logger.Info('Agent calculate simulation reward')
        self._logger.Info('------------------------------------')

        #Accumulate from the bottom to the top
        for layer in layer_bottom_up:
            #if we reach layer = 0, just break
            if layer == 0:
                break

            self._logger.Info('Calculate simulation reward over horizon = {}'.format(layer))

            #Get all nodes in this layer
            all_nodes_in_layer = self._histree.GetHistoryByLayer(layer)

            self._logger.Info('Nodes at this layer = {}'.format(all_nodes_in_layer))

            #Iterate each node in this layer of HisTree
            for node in all_nodes_in_layer:
                #Get parent node of current node
                parent_node = node.Parent

                self._logger.Debug('(node, parent) = ({},{})'.format(node, parent_node))

                #Calculate the immediate reward
                ary_belief = np.array(node.Belief)
                ary_immediate_reward = np.array(node.ImmediateRewardData)
                node.ImmediateReward = np.dot(ary_belief, ary_immediate_reward)

                self._logger.Debug('    Calculate immediate reward({}) = belief({}) * immediate reward({})'.format(node.ImmediateReward, ary_belief, ary_immediate_reward))

                if layer > 1:
                    #Get index of node as child node in parent node's child list,
                    #this is the index of parent node's Prob_o_s_a_Data
                    child_index = parent_node.GetChildIndex(node)

                    #Calculate temporal reward of this node with respect to its immediate reward
                    temp_reward = parent_node.Prob_o_s_a_Data[child_index] * node.ImmediateReward * pow((self._discount_factor), (layer - 1))

                    self._logger.Debug('    Parent node Prob_o_s_a_Data = {}'.format(parent_node.Prob_o_s_a_Data))
                    self._logger.Debug('    Temporal reward({}) = Parent_node.Prob_o_s_a_Data({}) * node.ImmediateReward({}) * {}^{}'.format(
                        temp_reward, parent_node.Prob_o_s_a_Data[child_index], node.ImmediateReward, self._discount_factor, (layer - 1)
                    ))

                    #Add temporal reward of this node and current accumulative reward of this node to parent node's current reward
                    parent_node.CurrentReward = temp_reward + node.CurrentReward

                    self._logger.Info('    parent_node.CurrentReward({}) = temporal reward({}) + node.CurrentReward({})'.format(
                        parent_node.CurrentReward, temp_reward, node.CurrentReward))
                else:
                    temp_reward = node.CurrentReward

                    node.CurrentReward = node.ImmediateReward + temp_reward

                    self._logger.Info('    node.FinalReward({}) = node.ImmediateReward({}) + node.CurrentReward({})'.format(
                        node.CurrentReward, node.ImmediateReward, temp_reward))

    """
    Return the normalized probability, since the estimated out beliefs might not be summed to 1
    """
    def NormalizeProbability(self, probs):
        normalized_probs = [0 for _ in range(len(probs))]

        total_prob = 0
        for b in probs:
            total_prob += b

        for i, b in enumerate(probs):
            normalized_probs[i] = b / total_prob
    
        return normalized_probs

    """
    Return parent nodes with regards to the same or different observation
    """
    def GetRelatedNodesByObservation(self, o, parent_nodes, the_same_as_o = 1):
        if (len(parent_nodes) == 1) and (parent_nodes[0].Parent == None):  #The root node
            return parent_nodes  #Return only the root node
        else:
            if the_same_as_o == 1:
                return [p for p in parent_nodes if (p.ObservationByActionTag.endswith(o.Name) == True)]
            else:
                return [p for p in parent_nodes if (p.ObservationByActionTag.endswith(o.Name) == False)]

    """
    Return parent nodes with regards to the given world state of s(input by caller in its observation o) to be the prior
    """
    def GetPriorNodesByObservation(self, o, world_s, parent, parent_nodes, the_same_as_world_state = 1, include_parent = 1):
        parent_nodes_o = None

        if (len(parent_nodes) == 1) and (parent_nodes[0].Parent == None):  #The root node
            return parent_nodes  #Return only the root node
        else:
            if the_same_as_world_state == 1:
                parent_nodes_o = [p for p in parent_nodes if (p.ObservationByActionTag.endswith(world_s.Name) == True)]
            else:
                parent_nodes_o = [p for p in parent_nodes if (p.ObservationByActionTag.endswith(world_s.Name) == False)]

        if (include_parent == 1): #and (o.Name != world_s.Name):
            if parent not in parent_nodes_o:
                parent_nodes_o.insert(0, parent)

        if (include_parent == 0):
            #Remove the parent node in the parent_nodes_o, if any
            if parent in parent_nodes_o:
                parent_nodes_o.remove(parent)

        return parent_nodes_o

    """
    Calculate the total probability of transiting from si to sj(represented by o) after action a has been taken
    """
    def GetTotalTransitiveProbability(self, a, sj, s_list, parent_nodes):
        #Get related transitive probability from si to sj by action a
        transitive_probability_list = [self._transition_model.Probability(si, sj, a) for si in s_list]

        total_transitive_probability = 0

        for p in parent_nodes:
            for i, b in enumerate(p.Belief):
                total_transitive_probability += transitive_probability_list[i] * b

        return total_transitive_probability

    """
    Do the belief update by action and observation and parent onodes,
    it returns the [b'(s1), b'(s2),..., b'(sn)] from prior b, where
    this input o is the world state we assume/believe we are in.
    """
    def UpdateBelief(self, a, o, s_list, parent_node, parent_nodes):
        """
        This input parameter o implies that we believe that we are in the state indicated by observation o
        """
        updated_belief = [0.0 for _ in range(len(s_list))]

        parents_nodes_o = None #[] #[0] the set of the same o, [1]the set of different o
        parents_nodes_o_s = None

        #parents_nodes_o.append(self.GetRelatedNodesByObservation(o, parent_nodes, 1))
        #parents_nodes_o.append(self.GetRelatedNodesByObservation(o, parent_nodes, 0))

        for i, s in enumerate(s_list):
            likeli = self._observation_model.Probability(s, o, a) #The probability that you make s in o(to be believed world state), after by action a

            #Calculate probability of making observation s,P(s|s), under world state o, by action a
            if o.Name == s.Name:
                if len(parent_nodes) == 2:
                    parents_nodes_o = [parent_node]
                else:
                    parents_nodes_o = self.GetPriorNodesByObservation(s, o, parent_node, parent_nodes, 1, 1)

                #We believe we make observation o, in state o(o=s), should choose parent nodes of the same observation o
                prob_transite_to_s = self.GetTotalTransitiveProbability(a, s, s_list, parents_nodes_o)

                prob_o_s_a = likeli * prob_transite_to_s
            else:
                if len(parent_nodes) == 2:  #for the case 2 parent nodes, when the given world state o is different from current enumerated b(s), this is not a good design...to be conti
                    parents_nodes_o = [parent_node]
                else:
                    parents_nodes_o = self.GetPriorNodesByObservation(s, o, parent_node, parent_nodes, 1, 1)

                #We believe we make observation o, in state s(o!=s), should choose parent nodes of the different observation o
                prob_transite_to_s = self.GetTotalTransitiveProbability(a, s, s_list, parents_nodes_o)

                prob_o_s_a = likeli * prob_transite_to_s

            self._logger.Info('b({})'.format(s))
            self._logger.Debug('  Nominator part:')
            self._logger.Debug('    Likeli of O(P({}|{})) in W_S({}) by A({}) = {}'.format(s, s, o, a, likeli))
            self._logger.Debug('    Total transitive probability to S({}) = {}'.format(s, prob_transite_to_s))
            self._logger.Debug('      Parent nodes for O(P({}|{})), W_S({}) by A({}):'.format(s, s, o, a))

            for p in parents_nodes_o:
                self._logger.Debug('        {}'.format(p))

            self._logger.Debug('    {}'.format(prob_o_s_a))

            #Build the parent node list to be used for the unvisited states
            parents_nodes_o_s = []

            for p in parent_nodes:
                if p not in parents_nodes_o:
                    parents_nodes_o_s.append(p)

            if len(parents_nodes_o_s) == 0:
                parents_nodes_o_s = [parent_node]

            #Calculate the total probability of making observation s, in all states s'(s_prime), by action a
            self._logger.Debug('  Denominator part:')

            prob_o_a = 0

            for s_prime in s_list: #s_prime is treated as world state in this loop
                if s_prime.Name == o.Name:
                    continue  #For we have enumerated this same state in nominator part, continue to next

                likeli = self._observation_model.Probability(s, s_prime, a)

                prob_transite_to_s_prime = self.GetTotalTransitiveProbability(a, s, s_list, parents_nodes_o_s)

                prob_o_a += likeli * prob_transite_to_s_prime

                """
                if o.Name == s_prime.Name:
                    #We believe we make observation s, in state s_prime, should choose parent nodes of the same observation o,
                    #containing the input parent node in it
                    parents_nodes_o_s = self.GetPriorNodesByObservation(s, s_prime, parent_node, parent_nodes, 1, 1)

                    prob_transite_to_s_prime = self.GetTotalTransitiveProbability(a, s, s_list, parents_nodes_o_s)

                    prob_o_a += likeli * prob_transite_to_s_prime
                else:
                    #We believe we make observation s, in state s_prime(o!=s_prime), should choose parent nodes of the different observation o,
                    #excluding the input parent node in it
                    parents_nodes_o_s = self.GetPriorNodesByObservation(s, s_prime, parent_node, parent_nodes, 1, 0)

                    prob_transite_to_s_prime = self.GetTotalTransitiveProbability(a, s, s_list, parents_nodes_o_s)

                    prob_o_a += likeli * prob_transite_to_s_prime
                """
                self._logger.Debug('    Likeli of O(P({}|{})) in W_S({}) by A({}) = {}'.format(s, s, s_prime, a, likeli))
                self._logger.Debug('    Total transitive probability to S({}) = {}'.format(s, prob_transite_to_s_prime))
                self._logger.Debug('      Parent nodes for O(P({}|{})), W_S({}) by A({}):'.format(s, s, s_prime, a))

                for p in parents_nodes_o_s:
                    self._logger.Debug('        {}'.format(p))

                self._logger.Debug('    {}'.format(prob_o_a))

            #Add nominator part to the denominator part to have a complete total probability
            prob_o_a += prob_o_s_a

            updated_belief[i] = prob_o_s_a / prob_o_a

            self._logger.Debug('{}'.format(updated_belief[i]))

        updated_belief = self.NormalizeProbability(updated_belief)

        self._logger.Info('normalize {}'.format(updated_belief))

        return updated_belief

    """
    The simulation evaluates out a convergent result in tree structure, according to which the agent
    can run or predict the optimal action.  It is the monotonic action manner with the tree structure
    represented in the aggregation of the same action a.
    """
    def Simulation(self, a_list, o_list, s_list):
        self._logger.Info('Agent simulation...')

        actions = a_list
        observations = o_list
        states = s_list
        index = 0

        #loop until we reach horizon_length
        for layer in range(self._horizon_length):
            self._logger.Info('------------------------------------')
            self._logger.Info('Agent simulation over horizon = {}'.format(layer))
            self._logger.Info('------------------------------------')

            #Get all nodes in each layer and make distinct evaluation
            parents = self._histree.GetHistoryByLayer(layer)

            self._logger.Info('All parent nodes:')

            for p in parents:
                self._logger.Info('  {}'.format(p))

            index = 0

            #Enumerate in the unit of each action
            for a in actions:
                #Generate new histree node in according to a,o combination
                if layer == 0:
                    p_a_list = parents  #It is the root node only
                else:
                    p_a_list = [p for p in parents if (p.ObservationByActionTag.startswith(a.Name) == True)]

                self._logger.Info('Parent nodes of A({}):'.format(a))

                for p in p_a_list:
                    self._logger.Info('  {}'.format(p))

                #Enumerate each parent of this same action
                for parent in p_a_list:
                    #Enumerate each observation after taking action a
                    for o in observations:
                        self._logger.Info('Enumerate A({}), O({}) from {}'.format(a, o, parent))

                        #This o is the to be believed world state
                        updated_belief = self.UpdateBelief(a, o, states, parent, p_a_list)

                        #Calculate the immediate reward during simulation phase
                        ret_dict = self.CalculateImmediateReward(updated_belief, a, s_list, o_list)

                        #Create HisTreeNode object for each a, o at this layer
                        obj_HisTreeNode = HisTreeNode(parent, a, o, updated_belief, (layer + 1), index)
                        obj_HisTreeNode.ImmediateRewardData = ret_dict['immediate_reward']
                        obj_HisTreeNode.Prob_o_s_a_Data = ret_dict['simulated_prob']

                        index += 1

                        #Add this new HisTreeNode object to HisTree at (layer + 1) 
                        self._histree.AddNodeInHistory((layer + 1), obj_HisTreeNode)

        #Calculate the simulated rewards with regard to each action
        self.CalculateSimulationReward()

    def Run(self):
        pass