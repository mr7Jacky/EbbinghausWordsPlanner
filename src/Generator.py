from datetime import datetime
from datetime import timedelta


class Generator:
    """
    Generate the plan
    """

    def __init__(self):
        self.plan = dict()
        self.ebbinghaus_curve = [0, 1, 2, 4, 7, 15]

    def append_dict(self, key, value):
        """
        Append value to key in dictionary
        :param key: date
        :param value: list name
        """
        if self.plan.get(key) is None:
            self.plan[key] = [value]
        else:
            self.plan.update({key: [value] + self.plan.get(key)})

    def generate_plan(self, tot_lists, start_date, list_name="List", reverse=False):
        """
        Generate plans with given info
        :type tot_lists: int
        :param tot_lists:
        :type start_date: datetime
        :param start_date:
        :type list_name: str
        :param list_name: list name
        :type reverse: bool
        :param reverse: whether reverse the sequence
        """
        for i in range(tot_lists):
            for j in self.ebbinghaus_curve:
                cur_data = start_date + timedelta(days=i+j)
                if reverse:
                    cur_list = tot_lists - i
                else:
                    cur_list = i + 1
                self.append_dict(cur_data, "%s %d" % (list_name, cur_list))

    def get_plan(self):
        """
        Get the generated plan
        :return: plan
        """
        return self.plan

    def clear_plan(self):
        self.plan.clear()


if __name__ == "__main__":
    x = datetime(2020, 11, 27)
    g = Generator()
    g.generate_plan(5, x, reverse=True)
    p = g.get_plan().keys()
    print(p)
