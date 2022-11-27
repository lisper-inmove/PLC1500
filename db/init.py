import pymysql


class Init:
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    password = '123456'
    db_name = "plc_machine"

    client = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password
    )

    def create_db(self):
        sql = """
        CREATE DATABASE IF NOT EXISTS plc_machine
        """
        cursor = self.client.cursor()
        cursor.execute(sql)

    def create_depth_test_db10(self):
        sql = """
        CREATE TABLE  IF NOT EXISTS depth_test_db10 (
        worker_number SMALLINT COMMENT "作业人员编号",
        station_type SMALLINT COMMENT "工位类型",
        station_number INT COMMENT "测试工位号",
        test_time_year SMALLINT UNSIGNED COMMENT "测试时间.YEAR",
        test_time_month TINYINT COMMENT "测试时间.MONTH",
        test_time_day TINYINT COMMENT "测试时间.DAY",
        test_time_weekday TINYINT COMMENT "测试时间.WEEKDAY",
        test_time_hour TINYINT COMMENT "测试时间.HOUR",
        test_time_minute TINYINT COMMENT "测试时间.MINUTE",
        test_time_second TINYINT COMMENT "测试时间.SECOND",
        test_time_nanosecond INT COMMENT "测试时间.NANOSECOND",
        test_one_falling_head INT COMMENT "测试点1落差",
        test_two_falling_head INT COMMENT "测试点2落差",
        test_three_falling_head INT COMMENT "测试点3落差",
        test_four_falling_head INT COMMENT "测试点4落差",
        standby_data INT COMMENT "备用数据",
        standby_data_1 INT COMMENT "备用数据1",
        station_shielding BOOLEAN COMMENT "工位屏蔽",
        status SMALLINT COMMENT "第0~2位为1时表示 运行中/报警中/急停中",
        product_exists TINYINT COMMENT "0位置1表示有产品;1位置1表示无产品",
        product_abnormal TINYINT COMMENT "0位置1表示正常产品;1位置1表示异常产品",
        work_status TINYINT COMMENT "0位置1表示工作开始;1位置1表示工作完成",
        test_result TINYINT COMMENT "测试结果",
        ranging_sensor INT COMMENT "1/2/3/4位表示测距传感器1/2/3/4的状态;",
        product_model INT COMMENT "产品型号",
        serial_number VARCHAR(255) COMMENT "产品编号"
        )
        """
        self.client.select_db(self.db_name)
        cursor = self.client.cursor()
        cursor.execute(sql)

    def create_depth_test_db11(self):
        sql = """
        CREATE TABLE  IF NOT EXISTS depth_test_db11 (
        worker_number SMALLINT COMMENT "作业人员编号",
        station_type SMALLINT COMMENT "工位类型",
        station_number INT COMMENT "测试工位号",
        test_time_year SMALLINT UNSIGNED COMMENT "测试时间.YEAR",
        test_time_month TINYINT COMMENT "测试时间.MONTH",
        test_time_day TINYINT COMMENT "测试时间.DAY",
        test_time_weekday TINYINT COMMENT "测试时间.WEEKDAY",
        test_time_hour TINYINT COMMENT "测试时间.HOUR",
        test_time_minute TINYINT COMMENT "测试时间.MINUTE",
        test_time_second TINYINT COMMENT "测试时间.SECOND",
        test_time_nanosecond INT COMMENT "测试时间.NANOSECOND",
        test_one_falling_head INT COMMENT "测试点1设定值",
        test_two_falling_head INT COMMENT "测试点2设定值",
        test_three_falling_head INT COMMENT "测试点3设定值",
        test_four_falling_head INT COMMENT "测试点4设定值",
        test_error INT COMMENt "测试误差",
        standby_data INT COMMENT "备用数据",
        standby_data_1 INT COMMENT "备用数据1",
        product_model INT COMMENT "产品型号"
        )
        """
        self.client.select_db(self.db_name)
        cursor = self.client.cursor()
        cursor.execute(sql)

    def create_auto_fill_ammo_db10(self):
        sql = """
        CREATE TABLE  IF NOT EXISTS auto_fill_ammo_db10 (
        worker_number SMALLINT COMMENT "作业人员编号",
        station_type SMALLINT COMMENT "工位类型",
        package_number INT COMMENT "组装工位号",
        package_finish_time_year SMALLINT UNSIGNED COMMENT "组装完成时间.YEAR",
        package_finish_time_month TINYINT COMMENT "组装完成时间.MONTH",
        package_finish_time_day TINYINT COMMENT "组装完成时间.DAY",
        package_finish_time_weekday TINYINT COMMENT "组装完成时间.WEEKDAY",
        package_finish_time_hour TINYINT COMMENT "组装完成时间.HOUR",
        package_finish_time_minute TINYINT COMMENT "组装完成时间.MINUTE",
        package_finish_time_second TINYINT COMMENT "组装完成时间.SECOND",
        package_finish_time_nanosecond INT COMMENT "组装完成时间.NANOSECOND",
        thickness_of_compensation_mat INT COMMENT "补偿垫测试厚度",
        package_combination_type INT COMMENT "组装组合类型",
        standby_data INT COMMENT "备用数据",
        standby_data_1 INT COMMENT "备用数据1",
        standby_data_2 INT COMMENT "备用数据2",
        standby_data_3 INT COMMENT "备用数据3",
        station_shielding BOOLEAN COMMENT "工位屏蔽",
        status SMALLINT COMMENT "第0~2位为1时表示 运行中/报警中/急停中",
        product_exists TINYINT COMMENT "0位置1表示有产品;1位置1表示无产品",
        product_abnormal TINYINT COMMENT "0位置1表示正常产品;1位置1表示异常产品",
        work_status TINYINT COMMENT "0位置1表示工作开始;1位置1表示工作完成",
        package_result TINYINT COMMENT "组装结果",
        cylinder_sensor INT COMMENT "1/2/3/4位分别表示1/2/3/4报警与否",
        standby_position TINYINT COMMENT "备用位/备用位1",
        product_model INT COMMENT "产品型号",
        serial_number VARCHAR(255) COMMENT "产品编号"
        )
        """
        self.client.select_db(self.db_name)
        cursor = self.client.cursor()
        cursor.execute(sql)

    def create_auto_fill_ammo_db11(self):
        sql = """
        CREATE TABLE  IF NOT EXISTS auto_fill_ammo_db11 (
        worker_number SMALLINT COMMENT "作业人员编号",
        station_type SMALLINT COMMENT "工位类型",
        package_number INT COMMENT "组装工位号",
        system_time_year SMALLINT UNSIGNED COMMENT "系统时间.YEAR",
        system_time_month TINYINT COMMENT "系统时间.MONTH",
        system_time_day TINYINT COMMENT "系统时间.DAY",
        system_time_weekday TINYINT COMMENT "系统时间.WEEKDAY",
        system_time_hour TINYINT COMMENT "系统时间.HOUR",
        system_time_minute TINYINT COMMENT "系统时间.MINUTE",
        system_time_second TINYINT COMMENT "系统时间.SECOND",
        system_time_nanosecond INT COMMENT "系统时间.NANOSECOND",
        product_model INT COMMENT "产品型号",
        model_of_compensation_mat INT COMMENT "补偿垫型号",
        thickness_of_compensation_mat INT COMMENT "补偿垫厚度",
        number_of_compensation_mat INT COMMENT "补偿垫数量"
        )
        """
        self.client.select_db(self.db_name)
        cursor = self.client.cursor()
        cursor.execute(sql)

    def create_engine_dismantle_db10(self):
        sql = """
        CREATE TABLE  IF NOT EXISTS engine_dismantle_db10 (
        worker_number SMALLINT COMMENT "作业人员编号",
        station_type SMALLINT COMMENT "工位类型",
        dismantle_number INT COMMENT "拆解工位号",
        dismantle_finish_time_year SMALLINT UNSIGNED COMMENT "拆解完成时间.YEAR",
        dismantle_finish_time_month TINYINT COMMENT "拆解完成时间.MONTH",
        dismantle_finish_time_day TINYINT COMMENT "拆解完成时间.DAY",
        dismantle_finish_time_weekday TINYINT COMMENT "拆解完成时间.WEEKDAY",
        dismantle_finish_time_hour TINYINT COMMENT "拆解完成时间.HOUR",
        dismantle_finish_time_minute TINYINT COMMENT "拆解完成时间.MINUTE",
        dismantle_finish_time_second TINYINT COMMENT "拆解完成时间.SECOND",
        dismantle_finish_time_nanosecond INT COMMENT "拆解完成时间.NANOSECOND",
        f1_motor_chou_set_value INT COMMENT "第一段电机杻矩设定值",
        f1_motor_chou_cur_value INT COMMENT "第一段电机杻矩当前值",
        f2_motor_chou_set_value INT COMMENT "第二段电机杻矩设定值",
        f2_motor_chou_cur_value INT COMMENT "第二段电机杻矩当前值",
        f3_motor_chou_set_value INT COMMENT "第三段电机杻矩设定值",
        f3_motor_chou_cur_value INT COMMENT "第三段电机杻矩当前值",
        f4_motor_chou_set_value INT COMMENT "第四段电机杻矩设定值",
        f4_motor_chou_cur_value INT COMMENT "第四段电机杻矩当前值",
        station_shielding BOOLEAN COMMENT "工位屏蔽",
        status SMALLINT COMMENT "第0~2位为1时表示 运行中/报警中/急停中",
        product_exists TINYINT COMMENT "0位置1表示有产品;1位置1表示无产品",
        product_abnormal TINYINT COMMENT "0位置1表示正常产品;1位置1表示异常产品",
        work_status TINYINT COMMENT "0位置1表示工作开始;1位置1表示工作完成",
        dismantle_result TINYINT COMMENT "拆解结果",
        motor_warning INT COMMENT "1/2/3/4/5/6/7位分别表示1/2/3/4/5/6/7报警与否",
        standby_position TINYINT COMMENT "备用位/备用位1",
        product_model INT COMMENT "产品型号",
        serial_number VARCHAR(255) COMMENT "产品编号"
        )
        """
        self.client.select_db(self.db_name)
        cursor = self.client.cursor()
        cursor.execute(sql)

    def create_engine_dismantle_db11(self):
        sql = """
        CREATE TABLE  IF NOT EXISTS engine_dismantle_db11 (
        worker_number SMALLINT COMMENT "作业人员编号",
        station_type SMALLINT COMMENT "工位类型",
        test_number INT COMMENT "当前测试工位号",
        test_time_year SMALLINT UNSIGNED COMMENT "系统时间.YEAR",
        test_time_month TINYINT COMMENT "系统时间.MONTH",
        test_time_day TINYINT COMMENT "系统时间.DAY",
        test_time_weekday TINYINT COMMENT "系统时间.WEEKDAY",
        test_time_hour TINYINT COMMENT "系统时间.HOUR",
        test_time_minute TINYINT COMMENT "系统时间.MINUTE",
        test_time_second TINYINT COMMENT "系统时间.SECOND",
        test_time_nanosecond INT COMMENT "系统时间.NANOSECOND",
        product_model INT COMMENT "产品型号",
        serial_number VARCHAR(255) COMMENT "产品编号",
        standby_data INT COMMENT "备用数据",
        standby_data_1 INT COMMENT "备用数据1",
        standby_data_2 INT COMMENT "备用数据2"
        )
        """
        self.client.select_db(self.db_name)
        cursor = self.client.cursor()
        cursor.execute(sql)

    def create_firebox_tighten_db10(self):
        sql = """
        CREATE TABLE  IF NOT EXISTS firebox_tighten_db10 (
        worker_number SMALLINT COMMENT "作业人员编号",
        station_type SMALLINT COMMENT "工位类型",
        tighten_number INT COMMENT "拧紧工位号",
        tighten_finish_time_year SMALLINT UNSIGNED COMMENT "拧紧完成时间.YEAR",
        tighten_finish_time_month TINYINT COMMENT "拧紧完成时间.MONTH",
        tighten_finish_time_day TINYINT COMMENT "拧紧完成时间.DAY",
        tighten_finish_time_weekday TINYINT COMMENT "拧紧完成时间.WEEKDAY",
        tighten_finish_time_hour TINYINT COMMENT "拧紧完成时间.HOUR",
        tighten_finish_time_minute TINYINT COMMENT "拧紧完成时间.MINUTE",
        tighten_finish_time_second TINYINT COMMENT "拧紧完成时间.SECOND",
        tighten_finish_time_nanosecond INT COMMENT "拧紧完成时间.NANOSECOND",
        f1_motor_chou_set_value INT COMMENT "第一段电机杻矩设定值",
        f1_motor_chou_cur_value INT COMMENT "第一段电机杻矩当前值",
        f2_motor_chou_set_value INT COMMENT "第二段电机杻矩设定值",
        f2_motor_chou_cur_value INT COMMENT "第二段电机杻矩当前值",
        f3_motor_chou_set_value INT COMMENT "第三段电机杻矩设定值",
        f3_motor_chou_cur_value INT COMMENT "第三段电机杻矩当前值",
        f4_motor_chou_set_value INT COMMENT "第四段电机杻矩设定值",
        f4_motor_chou_cur_value INT COMMENT "第四段电机杻矩当前值",
        station_shielding BOOLEAN COMMENT "工位屏蔽",
        status SMALLINT COMMENT "第0~2位为1时表示 运行中/报警中/急停中",
        product_exists TINYINT COMMENT "0位置1表示有产品;1位置1表示无产品",
        product_abnormal TINYINT COMMENT "0位置1表示正常产品;1位置1表示异常产品",
        work_status TINYINT COMMENT "0位置1表示工作开始;1位置1表示工作完成",
        tighten_result TINYINT COMMENT "拧紧结果",
        motor_warning INT COMMENT "电机报警:1/2/3/4/5/6/7位分别表示1/2/3/4/5/6/7报警与否",
        standby_position TINYINT COMMENT "备用位/备用位1",
        product_model INT COMMENT "产品型号",
        serial_number VARCHAR(255) COMMENT "产品编号"
        )
        """
        self.client.select_db(self.db_name)
        cursor = self.client.cursor()
        cursor.execute(sql)

    def create_firebox_tighten_db11(self):
        sql = """
        CREATE TABLE  IF NOT EXISTS firebox_tighten_db11 (
        worker_number SMALLINT COMMENT "作业人员编号",
        station_type SMALLINT COMMENT "工位类型",
        test_number INT COMMENT "当前测试工位号",
        test_time_year SMALLINT UNSIGNED COMMENT "系统时间.YEAR",
        test_time_month TINYINT COMMENT "系统时间.MONTH",
        test_time_day TINYINT COMMENT "系统时间.DAY",
        test_time_weekday TINYINT COMMENT "系统时间.WEEKDAY",
        test_time_hour TINYINT COMMENT "系统时间.HOUR",
        test_time_minute TINYINT COMMENT "系统时间.MINUTE",
        test_time_second TINYINT COMMENT "系统时间.SECOND",
        test_time_nanosecond INT COMMENT "系统时间.NANOSECOND",
        product_model INT COMMENT "产品型号",
        standby_data INT COMMENT "备用数据",
        standby_data_1 INT COMMENT "备用数据1",
        standby_data_2 INT COMMENT "备用数据2",
        shell_product_number VARCHAR(255) COMMENT "壳体产品编号",
        grain_product_number VARCHAR(255) COMMENT "药柱产品编号"
        )
        """
        self.client.select_db(self.db_name)
        cursor = self.client.cursor()
        cursor.execute(sql)

    def create_long_tail_tighten_db10(self):
        sql = """
        CREATE TABLE  IF NOT EXISTS long_tail_tighten_db10 (
        worker_number SMALLINT COMMENT "作业人员编号",
        station_type SMALLINT COMMENT "工位类型",
        tighten_number INT COMMENT "拧紧工位号",
        tighten_finish_time_year SMALLINT UNSIGNED COMMENT "拧紧完成时间.YEAR",
        tighten_finish_time_month TINYINT COMMENT "拧紧完成时间.MONTH",
        tighten_finish_time_day TINYINT COMMENT "拧紧完成时间.DAY",
        tighten_finish_time_weekday TINYINT COMMENT "拧紧完成时间.WEEKDAY",
        tighten_finish_time_hour TINYINT COMMENT "拧紧完成时间.HOUR",
        tighten_finish_time_minute TINYINT COMMENT "拧紧完成时间.MINUTE",
        tighten_finish_time_second TINYINT COMMENT "拧紧完成时间.SECOND",
        tighten_finish_time_nanosecond INT COMMENT "拧紧完成时间.NANOSECOND",
        f1_motor_chou_set_value INT COMMENT "第一段电机杻矩设定值",
        f1_motor_chou_cur_value INT COMMENT "第一段电机杻矩当前值",
        f2_motor_chou_set_value INT COMMENT "第二段电机杻矩设定值",
        f2_motor_chou_cur_value INT COMMENT "第二段电机杻矩当前值",
        f3_motor_chou_set_value INT COMMENT "第三段电机杻矩设定值",
        f3_motor_chou_cur_value INT COMMENT "第三段电机杻矩当前值",
        f4_motor_chou_set_value INT COMMENT "第四段电机杻矩设定值",
        f4_motor_chou_cur_value INT COMMENT "第四段电机杻矩当前值",
        station_shielding BOOLEAN COMMENT "工位屏蔽",
        status SMALLINT COMMENT "第0~2位为1时表示 运行中/报警中/急停中",
        product_exists TINYINT COMMENT "0位置1表示有产品;1位置1表示无产品",
        product_abnormal TINYINT COMMENT "0位置1表示正常产品;1位置1表示异常产品",
        work_status TINYINT COMMENT "0位置1表示工作开始;1位置1表示工作完成",
        tighten_result TINYINT COMMENT "拧紧结果",
        motor_warning INT COMMENT "电机报警:1/2/3/4/5/6/7位分别表示1/2/3/4/5/6/7报警与否",
        standby_position INT COMMENT "备用位/备用位1/备用位2/备用位3/备用位4",
        product_model INT COMMENT "产品型号",
        serial_number VARCHAR(255) COMMENT "产品编号"
        )
        """
        self.client.select_db(self.db_name)
        cursor = self.client.cursor()
        cursor.execute(sql)

    def create_long_tail_tighten_db11(self):
        sql = """
        CREATE TABLE  IF NOT EXISTS long_tail_tighten_db11 (
        worker_number SMALLINT COMMENT "作业人员编号",
        station_type SMALLINT COMMENT "工位类型",
        test_number INT COMMENT "当前测试工位号",
        test_time_year SMALLINT UNSIGNED COMMENT "系统时间.YEAR",
        test_time_month TINYINT COMMENT "系统时间.MONTH",
        test_time_day TINYINT COMMENT "系统时间.DAY",
        test_time_weekday TINYINT COMMENT "系统时间.WEEKDAY",
        test_time_hour TINYINT COMMENT "系统时间.HOUR",
        test_time_minute TINYINT COMMENT "系统时间.MINUTE",
        test_time_second TINYINT COMMENT "系统时间.SECOND",
        test_time_nanosecond INT COMMENT "系统时间.NANOSECOND",
        product_model INT COMMENT "产品型号",
        standby_data INT COMMENT "备用数据",
        standby_data_1 INT COMMENT "备用数据1",
        standby_data_2 INT COMMENT "备用数据2"
        )
        """
        self.client.select_db(self.db_name)
        cursor = self.client.cursor()
        cursor.execute(sql)


if __name__ == '__main__':
    obj = Init()
    obj.create_db()
    obj.create_depth_test_db10()
    obj.create_depth_test_db11()
    obj.create_auto_fill_ammo_db10()
    obj.create_auto_fill_ammo_db11()
    obj.create_engine_dismantle_db10()
    obj.create_engine_dismantle_db11()
    obj.create_firebox_tighten_db10()
    obj.create_firebox_tighten_db11()
    obj.create_long_tail_tighten_db10()
    obj.create_long_tail_tighten_db11()
