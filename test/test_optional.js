var co = require('co');
var expect = require('expect');
var run = require('./lib.js').run;

describe('Creative Engineer Exam #1 (Optional Tests)', () => {
	it('Case #11 should be caluculated', () => co(function*() {
		const input = [
			'2017/02',
			'2017/02/01 09:00-12:00 13:00-16:00'
		];
		const expected = [
			'0', '0', '0', '0', '0'
		];
		const actual = yield run('./run.sh', [], input.join('\n'));
		expect(actual).toEqual(expected);
	}));
	it('Case #12 should be caluculated', () => co(function*() {
		const input = [
			'2017/02',
			'2017/02/01 07:00-12:00 13:00-16:00'
		];
		const expected = [
			'1', '0', '0', '0', '0'
		];
		const actual = yield run('./run.sh', [], input.join('\n'));
		expect(actual).toEqual(expected);
	}));
	it('Case #13 should be caluculated', () => co(function*() {
		const input = [
			'2017/02',
			'2017/02/01 05:00-12:00 13:00-16:00'
		];
		const expected = [
			'1', '2', '0', '0', '0'
		];
		const actual = yield run('./run.sh', [], input.join('\n'));
		expect(actual).toEqual(expected);
	}));
	it('Case #14 should be caluculated', () => co(function*() {
		const input = [
			'2017/02',
			'2017/02/01 08:00-12:00 13:00-15:00'
		];
		const expected = [
			'0', '0', '0', '0', '0'
		];
		const actual = yield run('./run.sh', [], input.join('\n'));
		expect(actual).toEqual(expected);
	}));
	it('Case #15 should be caluculated', () => co(function*() {
		const input = [
			'2017/02',
			'2017/02/12 08:00-12:00 13:00-26:00'
		];
		const expected = [
			'0', '2', '4', '0', '15'
		];
		const actual = yield run('./run.sh', [], input.join('\n'));
		expect(actual).toEqual(expected);
	}));
	it('Case #16 should be caluculated', () => co(function*() {
		const input1 = [
			'2017/01',
			'2017/01/16 08:00-12:00 13:00-18:00',
			'2017/01/17 08:00-12:00 13:00-18:00',
			'2017/01/18 08:00-12:00 13:00-18:00',
			'2017/01/19 08:00-12:00 13:00-17:00',
			'2017/01/20 08:00-12:00 13:00-21:00'
		];
		const expected1 = [
			'4', '10', '0', '0', '0'
		];
		const actual1 = yield run('./run.sh', [], input1.join('\n'));
		expect(actual1).toEqual(expected1);

		const input2 = [
			'2017/01',
			'2017/01/16 08:00-12:00 13:00-18:00',
			'2017/01/17 08:00-12:00 13:00-18:00',
			'2017/01/18 08:00-12:00 13:00-18:00',
			'2017/01/19 08:00-12:00 13:00-17:00',
			'2017/01/20 08:00-12:00 13:00-21:00',
			'2017/01/23 08:00-12:00 13:00-18:00',
			'2017/01/24 08:00-12:00 13:00-18:00'
		];
		const expected2 = [
			'6', '12', '0', '0', '0'
		];
		const actual2 = yield run('./run.sh', [], input2.join('\n'));
		expect(actual2).toEqual(expected2);

		const input3 = [
			'2017/01',
			'2017/01/16 08:00-12:00 13:00-18:00',
			'2017/01/17 08:00-12:00 13:00-18:00',
			'2017/01/18 08:00-12:00 13:00-18:00',
			'2017/01/19 08:00-12:00 13:00-17:00',
			'2017/01/20 08:00-12:00 13:00-21:00',
			'2017/01/23 08:00-12:00 13:00-18:00',
			'2017/01/24 08:00-12:00 13:00-18:00',
			'2017/01/25 08:00-12:00 13:00-18:00',
			'2017/01/26 08:00-12:00 13:00-17:00'
		];
		const expected3 = [
			'8', '13', '0', '0', '0'
		];
		const actual3 = yield run('./run.sh', [], input3.join('\n'));
		expect(actual3).toEqual(expected3);

		const input4 = [
			'2017/01',
			'2017/01/16 08:00-12:00 13:00-18:00',
			'2017/01/17 08:00-12:00 13:00-18:00',
			'2017/01/18 08:00-12:00 13:00-18:00',
			'2017/01/19 08:00-12:00 13:00-17:00',
			'2017/01/20 08:00-12:00 13:00-21:00',
			'2017/01/23 08:00-12:00 13:00-18:00',
			'2017/01/24 08:00-12:00 13:00-18:00',
			'2017/01/25 08:00-12:00 13:00-18:00',
			'2017/01/26 08:00-12:00 13:00-17:00',
			'2017/01/27 08:00-12:00 13:00-21:00'
		];
		const expected4 = [
			'8', '20', '0', '0', '0'
		];
		const actual4 = yield run('./run.sh', [], input4.join('\n'));
		expect(actual4).toEqual(expected4);
	}));
});
