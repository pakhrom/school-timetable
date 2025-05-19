export const validTabs = [
	'replacements',
	'timetables',
	'callSchedule',
	'groups',
	'subjects',
	'teachers'
] as const;
export type TabType =
	| 'replacements'
	| 'timetables'
	| 'callSchedule'
	| 'groups'
	| 'subjects'
	| 'teachers';

export const currentTab: {
	tab: TabType;
} = $state({
	tab: 'replacements' // sadly, an exported state must be an object , because you cannot assign to exported variables
});
