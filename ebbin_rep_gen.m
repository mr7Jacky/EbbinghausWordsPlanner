% Ebbinghaus spaced repetition schedule generator
% 
% This script is used to generate a schedule for what you want to recite
% according to Ebbinghaus schedule.
% 
% Usage: 
%	First, set the parameters of tasks, number of days, the	Ebbinghaus
%	schedule and the date you start this plan. 
%	These parameters are all in cell PARAMETERS.
%	Then, run the script, you'll got the detailed repetion schedule in
%	variable ALLSCHEDULE.
% 
% Created by visionfans @ 2011.07.05
%% clear workspace
close all;clear;clc
%% parameters
% all the list you need to recite with vector form
allTasks = [1:31];
% the number of days you have
totalDays = 31;
% Ebbinghaus repetition schecule
ebbinSchedule = [1 2 4 7 13];
% the starting data with the form of 'month/day'
startingDate = datevec('07/05');
 
 
%% get the reciting list number of everyday task
everydayAmmount = ceil(length(allTasks)/(totalDays-ebbinSchedule(end)+1));
 
%% assign the date for every day
allSchedule = cell(totalDays,3);
 
for i=1:totalDays
	allSchedule{i,1} = sprintf('Day %2d',i);
	allSchedule{i,2} = datestr(startingDate + [0 0 i-1 0 0 0], 'mm-dd');
end
 
%% put all the tasks in every day schedule
firstDay = 1;
for i=1:everydayAmmount:allTasks(end)
	% lists to recite
	task = i:i+everydayAmmount-1;
	
	% put the task in allSchedule according to ebbinSchedule
	for j=1:length(ebbinSchedule)
		day = firstDay+ebbinSchedule(j)-1;
		allSchedule{day,3} = [allSchedule{day,3};task];
	end
	
	% next day 
	firstDay = firstDay + 1;
end

allSchedule