package com.crm.ai.dto;

import lombok.Data;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class AiResponseDto {
    private String answer;
    private String confidence;
}
