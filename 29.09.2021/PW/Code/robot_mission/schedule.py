from collections import defaultdict

from mesa.time import RandomActivation


class RandomActivationByKind(RandomActivation):
    """
    A scheduler which activates each kind of agent once per step, in random
    order, with the order reshuffled every step.

  

    Assumes that all agents have a step() method.
    """

    def __init__(self, model):
        super().__init__(model)
        self.agents_by_kind = defaultdict(dict)

    def add(self, agent):
        """
        Add an Agent object to the schedule

        Args:
            agent: An Agent to be added to the schedule.
        """

        self._agents[agent.unique_id] = agent
        agent_class = type(agent)
        self.agents_by_kind[agent_class][agent.unique_id] = agent

    def remove(self, agent):
        """
        Remove all instances of a given agent from the schedule.
        """

        del self._agents[agent.unique_id]

        agent_class = type(agent)
        del self.agents_by_kind[agent_class][agent.unique_id]

    def step(self, by_kind=True):
        """
        Executes the step of each agent type, one at a time, in random order.

        Args:
            by_kind: If True, run all agents of a single type before running
                      the next one.
        """
        if by_kind:
            for agent_class in self.agents_by_kind:
                self.step_kind(agent_class)
            self.steps += 1
            self.time += 1
        else:
            super().step()

    def step_kind(self, kind):
        """
        Shuffle order and run all agents of a given kind.

        Args:
            kind: Class object of the kind  to run.
        """
        agent_keys = list(self.agents_by_kind[kind].keys())
        self.model.random.shuffle(agent_keys)
        for agent_key in agent_keys:
            self.agents_by_kind[kind][agent_key].step()

    def get_kind_count(self, kind_class):
        """
        Returns the current number of agents of certain kind in the queue.
        """
        return len(self.agents_by_kind[kind_class].values())
