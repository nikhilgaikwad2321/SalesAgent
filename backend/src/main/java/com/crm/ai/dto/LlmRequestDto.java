package com.crm.ai.dto;

import lombok.Data;
import lombok.Builder;
import java.util.Map;

@Data
@Builder
public class LlmRequestDto {
    private String intent;
    private String query;
    private Map<String, String> filters;
}
