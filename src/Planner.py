from src.Generator import Generator
from datetime import datetime
from datetime import timedelta
import xlsxwriter


class Planner:
    """
    Output plan based on generator
    """

    def __init__(self):
        self.generator = Generator()
        self.tot_lists = 0
        self.start_date = None
        self.reverse = False
        self.list_name = "List"

    def generate(self):
        if self.tot_lists == 0 or self.start_date is None:
            print("ERROR: Not initialized")
            pass
        self.generator.generate_plan(self.tot_lists, self.start_date, self.list_name, self.reverse)

    def generate_excel(self, path, title):
        if len(self.generator.get_plan()) == 0:
            print("ERROR: Empty plan")
            pass
        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook(path)
        worksheet = workbook.add_worksheet()

        # Change format
        center = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
        bold = workbook.add_format({'bold': True})
        title_f = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter'})
        weekday = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday":3, "Thursday":4, "Friday": 5, "Saturday": 6}

        worksheet.set_column('A:G', 15, center)
        worksheet.merge_range('A1:G1', title, title_f)
        for col, name in enumerate(weekday):
            worksheet.write(1, col, name, bold)

        plan = self.generator.get_plan()
        duration = (max(plan.keys()) - min(plan.keys())).days
        m_height = [0] * ((duration // 7) + 1)
        for day in range(duration):
            cur_date = self.start_date + timedelta(days=day)
            row = ((day + weekday.get(self.start_date.strftime("%A"))) // 7) * 2 + 2
            col = weekday.get(cur_date.strftime("%A"))
            worksheet.write(row, col, cur_date.strftime("%x"))
            lists = plan.get(cur_date)
            if lists is not None:
                s = ''
                for i in range(len(lists)):
                    s += lists[i] + '\n'
                worksheet.write(row+1, col, s)
                idx = (row-1)//2
                print(idx, row+1)
                if m_height[idx] < len(lists):
                    m_height[idx] = len(lists)
                    worksheet.set_row(row+1, m_height[idx]*25)
        workbook.close()

    def set_tot_lists(self, value):
        """
        :type value: int
        """
        self.tot_lists = value

    def set_start_date(self, year, month, day):
        """
        :type year: int
        :type month: int
        :type day: int
        """
        self.start_date = datetime(year, month, day)

    def set_list_name(self, name):
        """
        :type name: str
        """
        self.list_name = name

    def set_reverse(self, reverse):
        """
        :type reverse: bool
        """
        self.reverse = reverse


if __name__ == "__main__":
    p = Planner()
    p.set_start_date(2020, 11, 16)
    p.set_tot_lists(10)
    p.generate()
    p.generate_excel("t.xlsx", 'sample')
