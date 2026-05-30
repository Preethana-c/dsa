def area_max(height):
    max_area=0
    area=0
    for i in range(len(height)):
        for j in range(i+1,len(height)):
            if height[i]<height[j]:

                area=height[i]*(j-i)
            else:
                area=height[j]*(j-i)
            max_area=max(max_area,area)
    return max_area