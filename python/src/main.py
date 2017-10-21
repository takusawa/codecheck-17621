# coding: utf-8
import sys
import jpholiday
import datetime
from datetime import datetime as dt

# 日付を取得し、日付に対応した曜日をかえす
def get_weekday(date):
	weekday = ["月","火","水","木","金","土","日"]
	d = dt.strptime(date, "%Y/%m/%d")
	return weekday[d.weekday()]

# 曜日、１週間単位の総労働時間、１日の労働時間、出勤時間、退勤時間から、１日における各残業時間数を返す
def working(day_of_week, total_work, work_sum, start, finish):
	#法定内残業時間数
	Overtime            = 0
	#法定外残業時間数
	LegalOvertime       = 0
	#深夜残業時間数
	MidnightOvertime    = 0
	#所定休日労働時間数
	HolidayWorking      = 0
	#法定休日労働時間数
	LegalHolidayWorking = 0

	#法定労働時間
	legal_work_standard = 8
	#法律が定める1週間あたりの労働時間
	week_work = 40
	#算出対象となる社員の休憩時間
	rest_time = 1
	#算出対象となる社員の就業開始時刻
	work_s = 8
	#算出対象となる社員の就業終了時刻
	work_e = 16
	#算出対象となる社員の実労働時間
	work_standard = 7
	#深夜残業の基準
	late_night = 22
	#1日の終わり
	day_change = 24

	#労働時間数
	legal_time = work_e + rest_time
	#法定内残業時間数
	overtime = legal_time - work_e
	#1週間の労働時間が40時間を超えるか
	if(total_work > week_work):
		LegalOvertime = (total_work - week_work)

	# 祝日の出社
	elif(day_of_week == "祝"):
		if(finish > day_change):
			LegalOvertime = (finish - day_change)
			MidnightOvertime = (finish - late_night)
			LegalHolidayWorking = (work_sum - (finish - day_change))
		elif(finish > late_night):
			MidnightOvertime = (finish - late_night)
			LegalHolidayWorking = work_sum
		else:
			LegalHolidayWorking = work_sum
	# 土曜日の出社
	elif(day_of_week == "土"):
		if(finish > day_change):
			MidnightOvertime = (finish - late_night)
			HolidayWorking = (work_sum - (finish - day_change))
			LegalHolidayWorking = (finish - day_change)
		elif(finish > late_night):
			MidnightOvertime = (finish - late_night)
			HolidayWorking = work_sum
		else:
			HolidayWorking = work_sum
	# 日曜日の出社
	elif(day_of_week == "日"):
		if(finish > day_change):
			LegalOvertime = (finish - day_change)
			MidnightOvertime = (finish - late_night)
			LegalHolidayWorking = (work_sum - (finish - day_change))
		elif(finish > late_night):
			MidnightOvertime = (finish - late_night)
			LegalHolidayWorking = work_sum
		else:
			LegalHolidayWorking = work_sum
	# 金曜日の出社かつ、日またぎ残業
	elif(day_of_week =="金" and finish > day_change):
		Overtime = overtime
		LegalOvertime = (day_change - legal_time)
		MidnightOvertime = (finish - late_night)
		HolidayWorking = (finish - day_change)

	#規定通りの出社時間、退社時間
	elif(start == work_s and finish == work_e):
		pass
	#規定通りでない出社時間、規定通りの退社時間
	elif(start != work_s and finish == work_e):
		if(work_sum == legal_work_standard):
			Overtime = overtime
		elif(work_sum < legal_work_standard):
			pass
		elif(work_sum > legal_work_standard):
			Overtime = overtime
			LegalOvertime += work_sum - legal_work_standard
	#出社時間、退社時間共に規定通りでない
	elif(start != work_s and finish != work_e):
		if(work_sum == legal_work_standard):
			Overtime = overtime
		elif(work_sum < legal_work_standard):
			pass
		elif(work_sum > legal_work_standard):
			regular_work = (start + rest_time + legal_work_standard)
			Overtime = (regular_work - work_e)
			LegalOvertime = (work_sum - legal_work_standard)

	#規定通りの出社時間、規定通りでない退社時間
	elif(start == work_s and finish != work_e):
		# 8時出社17時退社
		if(work_sum == legal_work_standard):
			Overtime = overtime
		# 8時出社、16時より前に退社
		elif(work_sum < legal_work_standard):
			pass
		# 17時以降の退社
		elif(work_sum > legal_work_standard):
			if(finish > late_night):
				Overtime = overtime
				LegalOvertime = (work_sum - legal_work_standard)
				MidnightOvertime = (finish - late_night)
			else:
				Overtime = overtime
				LegalOvertime = (work_sum - legal_work_standard)

	return (Overtime, LegalOvertime, MidnightOvertime, HolidayWorking, LegalHolidayWorking)

def total_work_time(data):
	#法定内残業時間数
	Overtime            = 0
	#法定外残業時間数
	LegalOvertime       = 0
	#深夜残業時間数
	MidnightOvertime    = 0
	#所定休日労働時間数
	HolidayWorking      = 0
	#法定休日労働時間数
	LegalHolidayWorking = 0

	#1週間
	a_week = 7
	#1週間単位での総労働時間を算出するための変数
	total_work = 0
	# 最初の月が記録される部分を除外する
	work_data = data[1:]
	# 労働日時を記録する変数
	day_array = []

	for hoge, work_times in enumerate(work_data):
		work_time = work_times.split(" ")

		# 日付を取得
		work_year = dt.strptime(work_time[0], "%Y/%m/%d").year
		work_month = dt.strptime(work_time[0], "%Y/%m/%d").month
		work_day = dt.strptime(work_time[0], "%Y/%m/%d").day
		# 曜日の取得
		if(jpholiday.is_holiday(datetime.date(work_year, work_month, work_day))):
			day_of_week = '祝'
		else:
			day_of_week = get_weekday(work_time[0])
		day_array.append(work_day)
		min_day = day_array[0]

		# 1日の労働開始時間、終了時間を格納する
		array = []
		# 1日の労働時間を格納する変数
		work_sum = 0
		for work in work_time[1:]:
			work_time = work.split("-")
			# 仕事の開始時間、終了時間を取得する変数
			work_start = 0
			work_stop  = 0
			for i, each_time in enumerate(work_time):
				# 仕事の開始時間、終了時間で分ける
				if(i % 2 == 0):
					work_start = dt.strptime(each_time, "%H:%M").hour
				else:
					# 労働終了時刻が24時を超えていないかチェック。超えていたら整数値に変換する
					try:
						work_stop = dt.strptime(each_time, "%H:%M").hour
					except ValueError:
						work_stop = int(each_time[0:2])

				# array に格納する時間が24時を超えていないかチェック
				try:
					time = dt.strptime(each_time, '%H:%M').hour
				except ValueError:
					time = int(each_time[0:2])

				array.append(time)
			# 就業開始時間と終了時刻から労働時間を算出し、1日の総労働時間に加える
			actual_work = work_stop - work_start
			work_sum += actual_work

		# 1週間単位で総労働時間をリセットする
		if(work_day - min_day >= a_week):
			day_array[0] = work_day
			total_work = 0
			total_work += work_sum
		else:
			total_work += work_sum

		# 業務開始時間、終了時間を記録した配列の先頭と末尾の要素番号を定義
		array_first = 0
		array_last  = len(array) - 1

		start  = array[array_first]
		finish = array[array_last]
		(Over_time, LegalOver_time, MidnightOver_time, Holiday_Working, LegalHoliday_Working) = working(day_of_week, total_work, work_sum, start, finish)
		Overtime += Over_time
		LegalOvertime += LegalOver_time
		MidnightOvertime += MidnightOver_time
		HolidayWorking += Holiday_Working
		LegalHolidayWorking += LegalHoliday_Working

	print(Overtime)
	print(LegalOvertime)
	print(MidnightOvertime)
	print(HolidayWorking)
	print(LegalHolidayWorking)

# testデータを受け取る
if __name__ == "__main__":
	data = sys.stdin.readlines()
	total_work_time(data)
