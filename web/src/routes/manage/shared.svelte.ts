export const currentTab: { tab: 'timetables' | 'subjects' | 'teachers' } = $state({
	tab: 'timetables' // sadly, an exported state must be an object , because you cannot assign to exported variables
});
