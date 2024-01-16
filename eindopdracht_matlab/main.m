% Compute power spectrum

% Generated by MATLAB(R) 9.13 and Signal Processing Toolbox 9.1.
% Generated on: 16-Jan-2024 14:26:34

% Parameters
timeLimits = [0 3.9998]; % seconds
frequencyLimits = [0 2500]; % Hz

%%
% Index into signal time region of interest
sig_ROI = sig(:);
sampleRate = 5000; % Hz
startTime = 0; % seconds
minIdx = ceil(max((timeLimits(1)-startTime)*sampleRate,0))+1;
maxIdx = floor(min((timeLimits(2)-startTime)*sampleRate,length(sig_ROI)-1))+1;
sig_ROI = sig_ROI(minIdx:maxIdx);

% Compute spectral estimate
% Run the function call below without output arguments to plot the results
pspectrum(sig_ROI, sampleRate, 'FrequencyLimits', frequencyLimits);

