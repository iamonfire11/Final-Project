
[audioIn,fs] = audioread("Sounds that attract cats - Meow to make cats come to you.wav");
 %If sound is stereo, convert to mono
[m, n] = size(audioIn); %gives dimensions of array where n is the number of stereo channels
 if n == 2
    y = audioIn(:, 1) + audioIn(:, 2);
    peakAmp = max(abs(y));
    y = y/peakAmp;
    %  check the L/R channels for orig. peak Amplitudes
    peakL = max(abs(audioIn(:, 1)));
    peakR = max(abs(audioIn(:, 2)));
    maxPeak = max([peakL peakR]);
    %apply x's original peak amplitude to the normalized mono mixdown
    y = y*maxPeak;
else
    y = audioIn; %it is mono
 end

%counter = 0;
sounds = classifySound(y,fs)
%for f=1:(max(size(sounds)))
    %if strcmp('Meow',sounds(f)) == 1
        %counter = counter+1;
    %end
%end
%counter
   


